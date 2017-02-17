import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# os.random: " This function returns random bytes from an OS-specific randomness source "
iv = os.urandom(16)
salt = os.urandom(16)

def hashing(password):
    hash = PBKDF2HMAC(algorithm=hashes.SHA256, length=32, salt=salt, iterations=10000, backend=default_backend())
    key = hash.derive(password.encode('ascii'))

    return key

def encrypt(key, iv, password):
    padder = padding.PKCS7(128).padder()
    padded_password = padder.update(password.encode('ascii')) + padder.finalize()

    ct = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encrypted = ct.encryptor()
    ciphertext = encrypted.update(padded_password) + encrypted.finalize()

    return ciphertext

def decrypt(key, iv, password):
    pt = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decrypted = pt.decryptor()
    plaintext = decrypted.update(password) + decrypted.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    unpadded_password = unpadder.update(plaintext) + unpadder.finalize()

    return unpadded_password

# Criptography usage

def EncryptExample():

    password = input("Type a password ('ASCII only'): ")
    
    _enc = encrypt(hashing(password), iv, password)
    print("\nEncryption:\nAs bytes: ", _enc, "\nAs HEX: ", _enc.hex())

    _dec = decrypt(hashing(password),iv, encrypt(hashing(password), iv, password))
    print("\nDecryption:\n", _dec.decode("utf-8"))

EncryptExample()
