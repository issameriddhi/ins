#ElGamal Digital Signature
import math

def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def primitive_root(num):
    primitive_no = None
    for n1 in range(2,num):
        remainders = [0 for i in range(num)]
        for power in range(1,num):
            if remainders[(n1**power) % num] == 0:
                remainders[(n1**power) % num] = 1
            else:
                break
        return n1
def relatively_prime(num):
    for n in range(2,num):
        if math.gcd(n,num-1) == 1:
            return n

def modular_inverse(A, M):
    # Extended Euclidean Algorithm to find the modular inverse
    for X in range(2, M):
        if (A * X  % M == 1):
            return X
    return -1

def elgamal(q,Xa,m):
    if not is_prime(q):
        print(f"q:{q} should be prime number")
        return
    alpha = primitive_root(q)
    #alpha = 10
    Ya = (alpha ** Xa) % q
    print(f"Public key of user: {q,alpha,Ya}")
    # Select a random integer k that is relatively prime to q-1
    k = relatively_prime(q)
    print("Relativeley prime: ",k)

    s1 = (alpha ** k) % q
    print("S1 : ",s1)
    k_inv = modular_inverse(k, q-1)
    #k_inv = k**-1 % (q-1)
    print("K inv: ",k_inv )
    s2 = (k_inv * (m - Xa * s1)) % (q-1)
    
    v1 = alpha**m % q
    v2 = ((Ya ** s1) * (s1 ** s2)) % q
    
    print("v1 (s1):", v1)
    print("v2 (s2):", v2)
q = int(input("Enter a prime number: "))
Xa = int(input("Enter the private key: "))
m = int(input("Enter the hash value (m): "))
elgamal(q,Xa,m)





