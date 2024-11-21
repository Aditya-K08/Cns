import random

alphabets = "abcdefghijklmnopqrstuvwxyz"


def encrypt(plaintext: str):

    l = list(alphabets)
    random.shuffle(l)
    key = "".join(l)

    ct = []

    for x in plaintext:
        if x.lower() in alphabets:
            y = key[alphabets.index(x.lower())]
            if x.isupper():
                y = y.upper()
            ct.append(y)
        else:
            ct.append(x)

    return ["".join(ct), key]


def decrypt(ciphertext: str, key: str):

    pt = []

    for x in ciphertext:
        if x.lower() in alphabets:
            y = alphabets[key.index(x.lower())]
            if x.isupper():
                y = y.upper()
            pt.append(y)
        else:
            pt.append(x)

    return "".join(pt)


ch = int(input('-----------------\n1. Encrypt\n2. Decrypt\n3. Exit\n-----------------\nEnter your choice: '))

if ch == 1:
    pt = input('Enter plaintext: ')
    ct = encrypt(pt)
    print(f'Ciphertext: {ct[0]}\nKey: {ct[1]}')

elif ch == 2:
    ct = input('Enter ciphertext: ')
    key = input('Enter key: ')
    pt = decrypt(ct, key)
    print(f'Plaintext: {pt}')

else:
    exit(0)