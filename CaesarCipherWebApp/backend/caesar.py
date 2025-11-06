# backend/caesar.py

def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts text using the Caesar Cipher.
    Mode 'decrypt' reverses the shift.
    """
    result = ""

    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            char_index = ord(char) - start
            shifted_index = (char_index + shift + 26) % 26
            shifted_char = chr(start + shifted_index)
            result += shifted_char
        else:
            result += char

    return result

if __name__ == '__main__':
    print(caesar_cipher("Hello World", 3, 'encrypt'))
    print(caesar_cipher("Khoor Zruog", 3, 'decrypt'))
