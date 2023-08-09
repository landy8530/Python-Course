import rsa
import base64

# Bob creates a key pair:
(bob_pub, bob_priv) = rsa.newkeys(512)
print(bob_pub)
print(bob_priv)


# Alice ecnrypts a message for Bob
# with his public key
credential = b'hello Bob!'
crypto = rsa.encrypt(credential, bob_pub)
base64Crypto = base64.b64encode(crypto)
print(base64Crypto)

# When Bob gets the message, he
# decrypts it with his private key:
base64Decrypto = base64.b64decode(base64Crypto)
message = rsa.decrypt(base64Decrypto, bob_priv)
print(message.decode('utf8'))
