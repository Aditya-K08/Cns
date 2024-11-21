import socket
import time

SERVER_ADDRESS = ('localhost', 12345)


def encrypt(plaintext, e, n):
    msg = [ord(c) - 31 for c in plaintext]
    ciphertext = [str(pow(c, e, n)) for c in msg]
    return '|'.join(ciphertext)


def sender():
    print("Connecting to the Receiver...")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect(SERVER_ADDRESS)
            print("Connected to the Receiver successfully!")

            data = client_socket.recv(1024).decode('utf-8')
            e, n = data.split(', ')
            e = int(e)
            n = int(n)

            print(f"e: {e}\nn: {n}")

            message = input('Enter message: ')

            start = time.time()
            ciphertext = encrypt(message, e, n)
            print(f"Ciphertext to be sent: {ciphertext}")
            end = time.time()
            print(f"Encryption Time: {(end-start):.10f}")

            client_socket.sendall(str(ciphertext).encode())
            print("Sent Ciphertext Successfully!!")
        except Exception as e:
            print(f"Exception caught: {e}")

    return


sender()