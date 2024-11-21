def encrypt(text, shift, key):
    encrypted_text = ""
    for char in text:
        shifted_char = chr((ord(char) + shift) % 256)
        encrypted_char = chr(ord(shifted_char) ^ key)
        encrypted_text += encrypted_char
    return encrypted_text


def decrypt(encrypted_text, shift, key):
    decrypted_text = ""
    for char in encrypted_text:
        xor_char = chr(ord(char) ^ key)
        original_char = chr((ord(xor_char) - shift) % 256)
        decrypted_text += original_char
    return decrypted_text


if __name__ == "__main__":
    plain_text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value: "))
    key = int(input("Enter the XOR key (0-255): "))

    encrypted = encrypt(plain_text, shift, key)
    print(f"Encrypted Text: {encrypted}")

    decrypted = decrypt(encrypted, shift, key)
    print(f"Decrypted Text: {decrypted}")
