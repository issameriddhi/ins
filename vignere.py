chars = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def encrypted(pt,k):
    ct = ""
    key_length = len(k)
    for i in range(len(pt)):
        ct += chars[(chars.index(pt[i].upper()) +  chars.index(k[i%key_length].upper()))%26]
    print(ct)
    
def decrypted(ct,k):
    pt = ""
    key_length = len(k)
    for i in range(len(ct)):
        pt += chars[(chars.index(ct[i].upper()) -  chars.index(k[i%key_length].upper()))%26]
    print(pt)

decrypted("OEESOZVOWTOKUIGN","HAT")