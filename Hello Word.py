# Original String
original_str="HELLO WORD"
print("Original String",original_str)
print("Character   |    ASCII   |    AND with 127   |    XOR with 127")
print("--------------------------------------------------------------------------------")
for char in  original_str:
    ascii_val=ord(char)
    and_result=ascii_val & 127
    xor_result=ascii_val ^ 127
    print(f"{char}    |     {ascii_val}    |      {and_result:3}      |       {xor_result:3}")