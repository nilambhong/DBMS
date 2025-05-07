import math

#step1
p=3
q=7

#step2
n=p*q
print("n=",n)

#step3
phi=(p-1)*(q-1)

#step4
e=2
while(e<phi):
    if(math.gcd(e,phi)==1):
        break
    else:
        e+=1
print("e=",e)

#step
k=2
d=((k*phi)+1)/e
print("d=",d)
print(f"public key {e,n}")
print(f"private key {d,n}")

#Example
Msg=11
print(f"Original message,{Msg}")

#Encryption
C=pow(Msg,e)
C=math.fmod(C,n)
print(f'Encrypted message:{C}')

#Decryption
M=pow(C,d)
M=math.fmod(M,n)
print(f'Decrypted message:{M} ')
