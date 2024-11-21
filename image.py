import os


def encrypt(image, n, key):
    encrypted_image = bytearray(n)
    for i in range(n):
        encrypted_image[i] = image[(i+key) % n]

    return encrypted_image


def decrypt(image, n, key):
    decrypted_image = bytearray(n)
    for i in range(n):
        decrypted_image[i] = image[(i-key) % n]

    return decrypted_image


def main():

    while True:
        choice = int(
            input('-----------------\n1. Encrypt\n2. Decrypt\n3. Exit\n-----------------\nYour Choice: '))

        if choice == 3:
            exit(0)
        path = input('Enter path of the image: ')
        key = int(input('Enter key: '))

        filename, ext = os.path.splitext(path)

        with open(path, 'rb') as f:
            image = bytearray(f.read())

        n = len(image)

        result = None
        output_path = None
        if choice == 1:
            result = encrypt(image, n, key)
            output_path = f"{filename}_encrypted{ext}"
        elif choice == 2:
            result = decrypt(image, n, key)
            output_path = f"{filename}_decrypted{ext}"

        with open(output_path, 'wb') as f:
            f.write(result)


if __name__ == "__main__":
    main()