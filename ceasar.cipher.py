letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if letter != ' ':
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = (index + key) % num_letters
                ciphertext += letters[new_index]
        else:
            ciphertext += ' '
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if letter != ' ':
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = (index - key) % num_letters
                plaintext += letters[new_index]
        else:
            plaintext += ' '
    return plaintext

def caesar_cipher(text, key, mode='encrypt'):
    if mode == 'encrypt':
        return encrypt(text, key)
    elif mode == 'decrypt':
        return decrypt(text, key)
    else:
        raise ValueError("Mode should be 'encrypt' or 'decrypt'")

print ("************* welcome to my ceasar cipher program*******************")
print()
print('Do you want to encrypt or decrypt your message (e/d): ', end='')
usr_input = input().lower()
print()

# Example usage based on user input
if usr_input == 'e':
    key = int(input("Enter the key: "))
    plaintext = input("Enter the message to encrypt: ")
    encrypted_text = caesar_cipher(plaintext, key, mode='encrypt')
    print("Encrypted:", encrypted_text)
elif usr_input == 'd':
    ciphertext = input("Enter the message to decrypt: ")
    key = int(input("Enter the key: "))
    decrypted_text = caesar_cipher(ciphertext, key, mode='decrypt')
    print("Decrypted:", decrypted_text)
else:
    print("Invalid input. Please enter 'e' to encrypt or 'd' to decrypt.")
