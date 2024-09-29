#key:anything,data: anything
def rc4(key, data):
    # Initialize the state
    S = list(range(256))
    j = 0
    key_length = len(key)

    # Key Scheduling Algorithm (KSA)
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]

    # Pseudo-Random Generation Algorithm (PRGA)
    i = 0
    j = 0
    output = []

    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        output.append(byte ^ K)

    return bytes(output)

# Taking user input for key and data
key = input("Enter the key: ").encode()  # Convert to bytes
data = input("Enter the data: ").encode()  # Convert to bytes

# Encryption
ciphertext = rc4(key, data)
print(f'Encrypted: {ciphertext}')

# Decryption (same function as encryption)
plaintext = rc4(key, ciphertext)
print(f'Decrypted: {plaintext.decode()}')
