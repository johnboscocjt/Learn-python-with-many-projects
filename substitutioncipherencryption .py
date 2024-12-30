# cyber security encryption

import random
import string

# chars = string.whitespace + string.punctuation + string.digits + string.ascii_letters
chars = " " + string.punctuation + string.digits + string.ascii_letters

# type cast the string into the list
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# character and the key used for encryption
# print(f"chars : {chars}")
# print(f"key : {key}")

# encryption
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    # get the letter that is i the same index
    cipher_text += key[index]
    
print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")




# decryption
cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    # get the letter that is i the same index
    plain_text += chars[index]
 
print(f"Encrypted message: {cipher_text}")
print(f"Original/decrypted message: {plain_text}")
