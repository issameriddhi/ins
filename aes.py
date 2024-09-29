#AES Algorithm, text:
from aes_cipher import *
data=input("Ente a string: ")
data_encrypter=DataEncrypter()
data_encrypter.Encrypt(data,"test_pwd")
enc_data=data_encrypter.GetEncryptedData()
print("Encrypted Text: \n",enc_data)
data_decrypter=DataDecrypter()
data_decrypter.Decrypt(enc_data, "test_pwd")
dec_data = data_decrypter.GetDecryptedData()
print("Decrypted Text: \n",dec_data)
