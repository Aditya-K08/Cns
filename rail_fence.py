def encryptRF(text: str, key: int):

    rail = [['\n' for i in range(len(text))] for j in range(key)]

    border = False
    row = col = 0

    for t in text:

        if (row == 0) or (row == key-1):
            border = not border

        rail[row][col] = t
        col += 1

        if border:
            row += 1
        else:
            row -= 1

    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])

    return "".join(result)


def decryptRF(text: str, key: int):

    rail = [['\n' for i in range(len(text))] for j in range(key)]

    border = None
    row = col = 0

    for x in range(len(text)):

        if row == 0:
            border = True
        if row == key-1:
            border = False

        rail[row][col] = '*'
        col += 1

        if border:
            row += 1
        else:
            row -= 1

    index = 0

    for i in range(key):
        for j in range(len(text)):
            if (rail[i][j] == '*' and index < len(text)):
                rail[i][j] = text[index]
                index += 1

    result = []
    row = col = 0
    for t in text:

        if row == 0:
            border = True
        elif row == key-1:
            border = False

        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1

        if border:
            row += 1
        else:
            row -= 1

        index = 0

    return "".join(result)


ch = int(input('Rail Fence Cipher\n----------------\n1. Encrypt\n2. Decrypt\n3. Exit\n----------------\nYour Choice: '))

if ch == 1:
    plaintext = input('Enter plaintext: ')
    key = int(input('Enter key: '))
    print(f'Ciphertext: {encryptRF(plaintext, key)}')
elif ch == 2:
    ciphertext = input('Enter ciphertext: ')
    key = int(input('Enter key: '))
    print(f'Plaintext: {decryptRF(ciphertext, key)}')
elif ch == 3:
    exit(0)
else:
    print('Invalid Input!!')