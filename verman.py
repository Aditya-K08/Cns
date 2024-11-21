import random
import string
import base64


def gen_key(x: int):
    key = ''.join(random.choice(string.ascii_letters + string.digits)
                  for _ in range(x))
    return key


def encrypt(plaintext: str, key: str):
    ciphertext = ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(plaintext, key))
    return base64.b64encode(ciphertext.encode()).decode()


def decrypt(ciphertext: str, key: str):
    decoded_ct = base64.b64decode(ciphertext).decode()
    plaintext = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(decoded_ct, key))
    return plaintext


ch = int(input('1. Encrypt\n2. Decrypt\n3. Exit\nYour Choice: '))

if ch == 1:
    pt = input('Enter plaintext: ')
    key = gen_key(len(pt))
    print(f'Key: {key}')
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