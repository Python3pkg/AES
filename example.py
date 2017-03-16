#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import main

"""

Criptography usage

Example_enc() 
    What does it do: It will ask for a message and password and encrypt the message
    Result: The encrypted message
     
Example_dec() 
    What does it do: It'll ask again for a password (The same used to encrypt)
    Result: The decrypted message

"""

# Example definitions

iv, salt = main.fortify()

def Example_enc():
    message     = input("Message (ASCCI)  : ")
    password    = input("Password (ASCII) : ")
    _enc = main.encrypt(main.hashing(password, salt), iv, message)
    
    return _enc
    
def Example_dec(enc_data):
    password = input("Password (ASCII) : ")
    
    return main.decrypt(main.hashing(password, salt), iv, enc_data)
    

# Example Calls

Enc = Example_enc()
print("Enc: ", Enc.hex())

Dec = Example_dec(Enc)
print(Dec.decode('ascii'))
