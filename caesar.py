def encrypt():
    pt = input('Enter plaintext: ')
    key = int(input('Enter Key: '))

    result = ''

    for i in pt:
        result += chr(((ord(i) + key - 31) % 128) + 31)
    print(f'Ciphertext: {result}')


def decrypt():
    ct = input('Enter ciphertext: ')
    key = int(input('Enter key: '))
    result = ''

    for i in ct:
        result += chr(((ord(i) - key - 31) % 128) + 31)
    print(f'Plaintext: {result}')


if __name__ == '__main__':
    ch = int(input(
        '------Caesar Cipher-----\n1. Encrypt\n2. Decrypt\n3. Exit\n-----------------\nYour Choice: '))
    if ch == 1:
        encrypt()
    elif ch == 2:
        decrypt()
    elif ch == 3:
        exit(0)
    else:
        print("Invalid Input!!")