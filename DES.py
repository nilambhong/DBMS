import pyDes
key="12345678"
des=pyDes.des(key,pyDes.ECB,padmode=pyDes.PAD_PKCS5)
data=input("Enter a string:")
encrpyted=des.encrypt(data)
print(" Encrypted message",encrpyted)

decrypted= des.decrypt(encrpyted)
print(" Descrypted message",decrypted)
