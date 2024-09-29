#dabba vala, text= anything, key= anyuthing smaller than 26 letter 
chars = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
def unique_letters(string):
    return ''.join(sorted(set(string), key=string.index))

def generate_key_matrix(key):
    matrix = [[],[],[],[],[]]
    key_index = {}
    new_chars = unique_letters(key)
    for i in chars:
        if i not in key.upper():
            new_chars += i
    for i in range(5):
        for j in range(5):
            key_index[new_chars[i*5+j].upper()] = (i,j)
            matrix[i].append(new_chars[i*5+j].upper())
    return (matrix, key_index)

def encrypt(plain_text, key):
    matrix,key_index = generate_key_matrix(key.upper())
    plain_text = "".join(plain_text.split())
    paired_text = []
    p1 = 0
    p2 = 1
    while p2<len(plain_text):
        txt1 = plain_text[p1].upper()
        txt2 = plain_text[p2].upper()
        if txt1 == "J":
            txt1 = "I"
        if txt2 == "J":
            txt2 = "I"
        
        if txt1 == txt2:
            paired_text.append([txt1, "X"])
            p1+=1
            p2+=1
            continue
        paired_text.append([txt1, txt2])
        p1 +=2
        p2 +=2
        if p1 == len(plain_text)-1:
            paired_text.append([plain_text[p1].upper(), "X"])
            break
    encrypted_text = ""
    for i in paired_text:
        if key_index[i[0]][0] == key_index[i[1]][0]:
            encrypted_text += matrix[key_index[i[0]][0]][(key_index[i[0]][1] + 1)%5] + matrix[key_index[i[1]][0]][(key_index[i[1]][1]+1)%5]
            continue
        if key_index[i[0]][1] == key_index[i[1]][1]:
            encrypted_text += matrix[(key_index[i[0]][0]+1)%5][key_index[i[0]][1]] + matrix[(key_index[i[1]][0]+1)%5][key_index[i[1]][1]]
            continue   
        encrypted_text += matrix[key_index[i[0]][0]][key_index[i[1]][1]] + matrix[key_index[i[1]][0]][key_index[i[0]][1]]
    print(encrypted_text)
    
def decrypt(cipher_text, key):
    matrix,key_index = generate_key_matrix(key)
    cipher_text = "".join(cipher_text.split())
    paired_text = []
    p1 = 0
    p2 = 1
    while p2<len(cipher_text):
        txt1 = cipher_text[p1].upper()
        txt2 = cipher_text[p2].upper()
        if txt1 == "J":
            txt1 = "I"
        if txt2 == "J":
            txt2 = "I"
        if txt1 == txt2:
            paired_text.append([txt1, "X"])
            p1+=1
            p2+=1
            continue
        paired_text.append([txt1, txt2])
        p1 +=2
        p2 +=2
        if p1 == len(cipher_text)-1:
            paired_text.append([cipher_text[p1].upper(), "X"])
            break
    decrypted_text = ""
    for i in paired_text:
        if key_index[i[0]][0] == key_index[i[1]][0]:
            decrypted_text += matrix[key_index[i[0]][0]][(key_index[i[0]][1] - 1)%5] + matrix[key_index[i[1]][0]][(key_index[i[1]][1]-1)%5]
            continue
        if key_index[i[0]][1] == key_index[i[1]][1]:
            decrypted_text += matrix[(key_index[i[0]][0]-1)%5][key_index[i[0]][1]] + matrix[(key_index[i[1]][0]-1)%5][key_index[i[1]][1]]
            continue   
        decrypted_text += matrix[key_index[i[0]][0]][key_index[i[1]][1]] + matrix[key_index[i[1]][0]][key_index[i[0]][1]]
    print(decrypted_text.replace("X","" ))

pt = input("Enter the plain text: ")
k1 = input("Enter the key: ")
encrypt(pt,k1)

ct = input("Enter the cipher text: ")
k2 = input("Enter the key: ")
decrypt(ct,k2)