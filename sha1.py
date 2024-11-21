import hashlib

def calculate_sha1(message: str):
    sha1_hash = hashlib.sha1()

    sha1_hash.update(message.encode())

    return sha1_hash.hexdigest()

def transmit_message():
    message = input("Enter the message to be transmitted: ")

    message_hash = calculate_sha1(message)
    
    print(f"SHA-1 Hash of the message: {message_hash}")

    received_message = message
    received_hash = calculate_sha1(received_message)
    
    if received_hash == message_hash:
        print("Integrity check passed: The message has not been tampered with!")
    else:
        print("Integrity check failed: The message may have been tampered with!")

if __name__ == "__main__":
    transmit_message()
