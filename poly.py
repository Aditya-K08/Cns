def encrypt(plaintext: str, key: str):
    key_len = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_as_int = [ord(i) for i in plaintext]
    ciphertext = ''

    for i in range(len(plaintext)):
        if plaintext[i].islower():
            value = chr((plaintext_as_int[i] + key_as_int[i %
                                                          key_len] - 2 * ord('a')) % 26 + ord('a'))
            ciphertext += value
        elif plaintext[i].isupper():
            value = chr((plaintext_as_int[i] + key_as_int[i %
                                                          key_len] - 2 * ord('A')) % 26 + ord('A'))
            ciphertext += value
        else:
            ciphertext += plaintext[i]

    return ciphertext


def decrypt(ciphertext: str, key: str):
    key_len = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_as_int = [ord(i) for i in ciphertext]
    plaintext = ''

    for i in range(len(ciphertext)):

        if ciphertext[i].islower():
            value = chr((ciphertext_as_int[i] - key_as_int[i %
                                                           key_len] + 26) % 26 + ord('a'))
            plaintext += value
        elif ciphertext[i].isupper():
            value = chr((ciphertext_as_int[i] - key_as_int[i %
                                                           key_len] + 26) % 26 + ord('A'))
            plaintext += value
        else:
            plaintext += ciphertext[i]

    return plaintext


ch = int(input(
    '------------\n1. Encrypt\n2. Decrypt\n3. Exit\n------------\nYour Choice: '))

if ch == 1:
    pt = input('Enter plaintext: ')
    key = input('Enter key: ')
    ct = encrypt(pt, key)
    print(f'Ciphertext: {ct}')
elif ch == 2:
    ct = input('Enter Ciphertext: ')
    key = input('Enter key: ')
    pt = decrypt(ct, key)
    print(f'Plaintext: {pt}')
elif ch == 3:
    exit(0)
else:
    print('Invalid Input')