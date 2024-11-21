import socket
import time

SERVER_ADDRESS = ('localhost', 12345)


def isPrime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5)+1):
        if x % i == 0:
            return False
    return True


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def co_prime(phi):
    for i in range(2, phi-1):
        if gcd(i, phi) == 1:
            return i
    return


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b//a) * x1
    y = x1
    return gcd, x, y


def mod_inverse(e, phi):
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("No inverse found!")
    return x


def decrypt(ciphertext, d, n):
    chunks = ciphertext.split('|')
    pt_chunks = [pow(int(c), d, n) for c in chunks]
    message = [chr(c+31) for c in pt_chunks]
    plaintext = ''.join(message)
    return plaintext


def receiver():
    print("Waiting for Sender to connect...\n")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(SERVER_ADDRESS)
        server_socket.listen(1)
        print(f"Receiver listening on {SERVER_ADDRESS}...\n")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected to Sender at {addr}")

            key_start = time.time()
            while True:
                p = int(input('Enter p (prime number): '))
                if not isPrime(p):
                    print(f"p is not prime.")
                else:
                    break

            while True:
                q = int(input('Enter q (prime number): '))
                if not isPrime(q):
                    print("q is not prime")
                else:
                    break

            n = p * q
            phi = (p - 1) * (q - 1)

            e = co_prime(phi)
            d = mod_inverse(e, phi)

            print(f"Generated keys:\ne: {e}\nn: {n}\nd: {d}\n")
            key_end = time.time()
            print(f"Decryption Time: {(key_end-key_start):.10f}")

            conn.sendall(f"{e}, {n}".encode())
            print("Public Key sent to the sender.\n")

            data = conn.recv(1024)
            dec_start = time.time()
            ciphertext = data.decode('utf-8')
            print(f"Received Ciphertext: {ciphertext}")

            message = decrypt(ciphertext, d, n)
            dec_end = time.time()
            print(f"Decryption Time: {(dec_end-dec_start):.20f}")
            print(f"Message: {message}")

    return


receiver()