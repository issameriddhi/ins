chars = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def encryption(pt,k):
    ct = ""
    for i in range(len(pt)): # 0.....len(pt) -1 
        ct += chars[(chars.index(pt[i].upper()) + chars.index(k[i].upper()))%26]
    print("Cipher text: ",ct)
    
def decryption(ct,k):
    pt = ""
    for i in range(len(ct)):
        pt += chars[(chars.index(ct[i].upper()) - chars.index(k[i].upper()))%26]
    print("Plain text: ",pt)

pt = input("Enter the plain text: ")
k1 = input("Enter the key: ")
encryption(pt,k1)

ct = input("Enter the cipher text: ")
k2 = input("Enter the key: ")
decryption(ct,k2)
