#Step1: Key identify (char or number)
#Step2: PT+K (PT letter index AND key index)
#Step3: (PT + K) % 26 (Do this for all plain text letters)

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def encryption(pt,k):
    ct= ''
    # To check wether the key is string or not
    if k.isalpha():
        k = chars.index(k)
    else:
        k = int(k)
    for letter in pt.upper():
        ct += chars[(chars.index(letter) + k) % 26]
    return ct

def decryption(ct,k):
    pt= ''
    # To check wether the key is string or not
    if k.isalpha():
        k = chars.index(k)
    else:
        k = int(k)
    for letter in ct.upper():
        pt += chars[(chars.index(letter) - k) % 26]
    print("Decrypted text: ",pt)
    
pt = input("Enter the plain text: ")
k1 = input("Enter the key: ")
ct = encryption(pt,k1)
print("Cipher Text: ",ct)
decryption(ct,k1)
        
