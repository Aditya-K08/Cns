import rsa
import hashlib

(pubkey_X, privkey_X) = rsa.newkeys(512)  
(pubkey_Y, privkey_Y) = rsa.newkeys(512)  

def hash_message(message):
    return hashlib.sha256(message.encode()).hexdigest()

def sign_message(hash_value, private_key):
    return rsa.sign(hash_value.encode(), private_key, 'SHA-256')

def verify_signature(hash_value, signature, public_key):
    try:
        rsa.verify(hash_value.encode(), signature, public_key)
        return True
    except rsa.VerificationError:
        return False

def send_message(message):
    print("\n--- Sender (X) ---")
    
    message_hash = hash_message(message)
    print(f"Hash of the message: {message_hash}")
    
    signature = sign_message(message_hash, privkey_X)
    print(f"Digital Signature: {signature.hex()}")

    encrypted_message = rsa.encrypt(message.encode(), pubkey_Y)
    print(f"Encrypted Message: {encrypted_message.hex()}")

    return encrypted_message, signature

def receive_message(encrypted_message, signature):
    print("\n--- Receiver (Y) ---")
    
    decrypted_message = rsa.decrypt(encrypted_message, privkey_Y).decode()
    print(f"Decrypted Message: {decrypted_message}")

    received_hash = hash_message(decrypted_message)
    is_valid = verify_signature(received_hash, signature, pubkey_X)

    if is_valid:
        print("Signature is valid. Message integrity confirmed!")
    else:
        print("Signature verification failed. Message may be tampered.")

if __name__ == "__main__":
    message = input("Enter the message to send: ")
    
    encrypted_message, signature = send_message(message)
    
    receive_message(encrypted_message, signature)
