# Caesar Cipher
# Encryption and Decryption

def encrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char

    return result


def decrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift - key) % 26 + shift)
        else:
            result += char

    return result


# Input
plaintext = input("Enter plaintext: ")
key = int(input("Enter key: "))

# Encryption
ciphertext = encrypt(plaintext, key)
print("Encrypted text:", ciphertext)

# Decryption
original_text = decrypt(ciphertext, key)
print("Decrypted text:", original_text)





# Vigenere Cipher
# Encryption and Decryption

def encrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')

            result += chr((ord(char) - base + shift) % 26 + base)

            key_index += 1
        else:
            result += char

    return result


def decrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')

            result += chr((ord(char) - base - shift) % 26 + base)

            key_index += 1
        else:
            result += char

    return result


# Input
plaintext = input("Enter plaintext: ")
key = input("Enter keyword: ")

# Encryption
ciphertext = encrypt(plaintext, key)
print("Encrypted text:", ciphertext)

# Decryption
original_text = decrypt(ciphertext, key)
print("Decrypted text:", original_text)
