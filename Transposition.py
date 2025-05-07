def encrypt_transposition(message,key):
    ciphertext=['']*key
    for col in range(key):
        pointer=col
        while pointer< len(message):
            ciphertext[col]+=message[pointer]
            pointer+=key
    return ''.join(ciphertext)

def decrypt_transposition(ciphertext,key):
    num_of_columns=key
    num_of_rows=-(-len(ciphertext) //key)
    num_of_shaded_boxes=num_of_columns*num_of_rows-len(ciphertext)
    plaintext=['']*num_of_rows
    col=0
    row=0

    for symbol in ciphertext:
        plaintext[row]+= symbol
        row+=1

        if(row==num_of_rows)or(row==num_of_rows-1 and col>=num_of_columns-num_of_shaded_boxes):
            row=0
            col+=1
    return ''.join(plaintext)

# Example
message="HELLOWORD"
print("Original message",message)
key=6
key= len("Vanita")
encryption=encrypt_transposition(message,key)
print("encrypted message",encryption)
decryption=decrypt_transposition(encryption,key)
print("decrypted message",decryption)

