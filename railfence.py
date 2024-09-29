def encryption(pt,k):
    pt = ("".join(pt.split())).upper()
    ct = ""
    for i in range(k):
        ct += pt[i::k] # i = 0,1,2,3
        print(ct) # For printing each row
    print(ct)

def decryption(ct,k):
    pt = ""
    if len(ct) % k == 0:
        _k = int(len(ct) / k)
    else:
        _k = int(len(ct) / k + 1)
    print(_k)
    for i in range(_k):
        pt += ct[i::_k] # i = 0,1,2,3
    print(pt)
    
encryption("ITS RAining heavily today",3)