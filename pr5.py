from math import gcd
from sympy import isprime

def is_prime(n):
    for i in range(2,n/2 + 1):
        if n%i==0:
            return False
    return True
p = int(input("Enter first prime number(p): "))
q = int(input("Enter second prime number(q): "))

if not(isprime(p) and isprime(q)):
    print("P and Q should be prime numbers")

n = p * q
phi = (p - 1) * (q - 1)

#e calculation
e = 2
while(e < phi):
    if(gcd(e, phi) == 1):
        break
    else:
        e += 1

#d calculation
d = 2
while(True):
    if(((d*e) % phi)== 1):
        break
    else:
        d += 1
print(f"Public key: {e,n} ")      
print(f"Private key: {d,n} ")      

M = int(input("Enter plaintext: "))
if (M >= n):
    raise Exception("Error! M is greater than n(p*q)!")
C = ((M ** e)% n)
print("Ciphertext = ", C)
PT = ((C ** d)% n)
print("Plaintext = ", PT)
