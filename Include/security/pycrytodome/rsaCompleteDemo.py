from Crypto.PublicKey import RSA
import Crypto.Signature.PKCS1_v1_5 as sign_PKCS1_v1_5  # 用于签名/验签
from Crypto.Cipher import PKCS1_v1_5  # 用于加密
from Crypto import Random
from Crypto import Hash

# 手动生成一个密钥对(项目中的密钥对一般由开发来生成)，生成密钥对的时候，可以指定生成的长度，一般推荐使用1024bit，
# 1024bit的rsa公钥，最多只能加密117byte的数据，数据流超过这个数则需要对数据分段加密，
# 目前1024bit长度的密钥已经被证明了不够安全，尽量使用2048bit长度的密钥，2048bit长度密钥最多能加密245byte长度的数据
# 计算长度公式：密钥长度 / 8 - 11 = 最大加密量(单位 bytes)
# 下面生成一对2048bit的密钥：
x = RSA.generate(2048)
# y = RSA.generate(2048, Random.new().read)   #也可以使用伪随机数来辅助生成

s_key = x.export_key()  # 私钥
g_key = x.publickey().export_key()  # 公钥
# print("私钥：", s_key)
# print("公钥：", g_key)

# 写入文件
# with open("c.pem", "wb") as x:
#     x.write(s_key)
# with open("d.pem", "wb") as x:
#     x.write(g_key)

# 从文件导入密钥 -- 通过私钥生成公钥  (公钥不会变 -- 用于只知道私钥的情况)--2
# with open('c.pem','rb')as x:
#     s_key = RSA.importKey(x.read())
# # new_g_key = s_key.publickey().export_key()
# # print(new_g_key)
#
# cert = s_key.export_key("DER")  #生成证书 -- 它和私钥是唯一对应的
# print(cert)

# 实现RSA 非对称加解密
my_private_key = s_key  # 私钥
my_public_key = g_key  # 公钥

# 使用公钥 - 私钥对信息进行"加密" + "解密"
'''
作用：对信息进行公钥加密，私钥解密。
应用场景：
    A想要加密传输一份数据给B，担心使用对称加密算法易被他人破解（密钥只有一份，一旦泄露，则数据泄露），故使用非对称加密。
    信息接收方可以生成自己的秘钥对，即公私钥各一个，然后将公钥发给他人，私钥自己保留。

    A使用公钥加密数据，然后将加密后的密文发送给B，B再使用自己的私钥进行解密，这样即使A的公钥和密文均被第三方得到，
    第三方也要知晓私钥和加密算法才能解密密文，大大降低数据泄露风险。
'''


def encrypt_with_rsa(plain_text):
    # 先公钥加密
    cipher_pub_obj = PKCS1_v1_5.new(RSA.importKey(my_public_key))
    _secret_byte_obj = cipher_pub_obj.encrypt(plain_text.encode())

    return _secret_byte_obj


def decrypt_with_rsa(_secret_byte_obj):
    # 后私钥解密
    cipher_pri_obj = PKCS1_v1_5.new(RSA.importKey(my_private_key))
    _byte_obj = cipher_pri_obj.decrypt(_secret_byte_obj, Random.new().read)
    plain_text = _byte_obj.decode()

    return plain_text


def execute_without_signature():
    # 加解密验证
    text = "I love CA!"
    assert text == decrypt_with_rsa(encrypt_with_rsa(text))
    print("rsa test success！")


# 使用私钥 - 公钥对信息进行"签名" + "验签"
'''
作用：对解密后的文件的完整性、真实性进行验证（繁琐但更加保险的做法，很少用到）
应用场景：
    A有一私密文件欲加密后发送给B，又担心因各种原因导致B收到并解密后的文件并非完整、真实的原文件（可能被篡改或丢失一部分），
    所以A在发送前对原文件进行签名，将[签名和密文]一同发送给B让B收到后用做一下文件的[解密 + 验签],
    均通过后-方可证明收到的原文件的真实性、完整性。

'''


def to_sign_with_private_key(plain_text):
    # 私钥签名
    signer_pri_obj = sign_PKCS1_v1_5.new(RSA.importKey(my_private_key))
    rand_hash = Hash.SHA256.new()
    rand_hash.update(plain_text.encode())
    signature = signer_pri_obj.sign(rand_hash)

    return signature


def to_verify_with_public_key(signature, plain_text):
    # 公钥验签
    verifier = sign_PKCS1_v1_5.new(RSA.importKey(my_public_key))
    _rand_hash = Hash.SHA256.new()
    _rand_hash.update(plain_text.encode())
    verify = verifier.verify(_rand_hash, signature)

    return verify  # true / false


def execute_with_signature():
    # 签名/验签
    text = "I love CA!"
    assert to_verify_with_public_key(to_sign_with_private_key(text), text)
    print("rsa Signature verified!")


if __name__ == '__main__':
    execute_without_signature()  # 只加密不签名

    execute_with_signature()  # 只签名不加密


# 二者结合使用更佳
'''
如果是加密的同时又要签名，这个时候稍微有点复杂。
1、发送者和接收者需要各持有一对公私钥，也就是4个钥匙。
2、接收者的公私钥用于机密信息的加解密
3、发送者的公私钥用于机密信息的签名/验签
4、接收者和发送者都要提前将各自的[公钥]告知对方。
'''