from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# 2048 is the number of bits for RSA
keys = RSA.generate(2048)

publicKey = keys.publickey()
publicKeyPEM = publicKey.exportKey()
print("\n", publicKeyPEM.decode('ascii'))


privateKeyPEM = keys.exportKey()
print("\n", privateKeyPEM.decode('ascii'))

# Your secret text
secretMessage = 'This is your secret'

# encrypt the message with the RSA public key
encryptor = PKCS1_OAEP.new(publicKey)
encrypted = encryptor.encrypt(secretMessage.encode())
print("\nEncrypted:", base64.b64encode(encrypted).decode('ascii'))

# decrypt the message with the RSA private key
decryptor = PKCS1_OAEP.new(keys)
decrypted = decryptor.decrypt(encrypted)
print('\nDecrypted Message:', decrypted.decode())

