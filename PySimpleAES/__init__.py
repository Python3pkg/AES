#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class PySimpleAES:
    
    def fortify(self):
        try:
            iv = os.urandom(16)
            salt = os.urandom(16)
            return iv, salt
        
        except BaseException as e:
            print('ERROR Salting: %s' % str(e))
            return
    
    def hashing(self, password, salt):
        try:
            hash = PBKDF2HMAC(algorithm=hashes.SHA256, length=32, salt=salt, iterations=10000, backend=default_backend())
            key = hash.derive(password.encode('ascii'))
            return key
        
        except BaseException as e:
            print('ERROR Hashing: %s')
            return
    
    def encrypt(self, key, iv, msg):
        try:
            padder = padding.PKCS7(128).padder()
            padded_password = padder.update(msg.encode('ascii')) + padder.finalize()
            ct = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            encrypted = ct.encryptor()
            ciphertext = encrypted.update(padded_password) + encrypted.finalize()
            return ciphertext
        
        except BaseException as e:
            print('ERROR Encrypting: %s' % str(e))
            return    
    
    def decrypt(self, key, iv, password):
        try:
            pt = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            decrypted = pt.decryptor()
            plaintext = decrypted.update(password) + decrypted.finalize()
            unpadder = padding.PKCS7(128).unpadder()
            unpadded_password = unpadder.update(plaintext) + unpadder.finalize()
            return unpadded_password
        
        except BaseException as e:
            print('ERROR Decrypting: %s' % str(e))
            return

    
    
    
    
    
    
    
