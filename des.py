#Des algorithm / text: anything  key :8 bytes long
from pyDes import *
data = input("Enter a string: ")
bin_data = data.encode()
key = input("Enter a key: ")
bin_key = key.encode()  
k = des(key, padmode=PAD_PKCS5)
cipher_data = k.encrypt(data)
print("Cipher Data: \n",cipher_data)
print("Decrypted Data: \n",k.decrypt(cipher_data))