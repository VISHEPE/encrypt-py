from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_message(key, message):
    f = Fernet(key)
    cipher_text = f.encrypt(message.encode())
    return cipher_text

def decrypt_message(key, cipher_text):
    f = Fernet(key)
    plain_text = f.decrypt(cipher_text)
    return plain_text

if __name__ == "__main__":
    key = generate_key()
    message = "This is a secret message."
    cipher_text = encrypt_message(key, message)
    print("Encrypted message:", cipher_text)
    plain_text = decrypt_message(key, cipher_text)
    print("Decrypted message:", plain_text)