#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyAES import PySimpleAES

"""

Criptography usage

Example_enc() 
    What does it do: It will ask for a message and password and encrypt the message
    Result: The encrypted message
     
Example_dec() 
    What does it do: It'll ask again for a password (The same used to encrypt)
    Result: The decrypted message

"""

# Defining your own class

class MyAES(PySimpleAES):

    def __init__(self):
        self.iv, self.salt = self.fortify()

    def Example_enc(self):
        message     = input("Message (ASCCI)  : ")
        password    = input("Password (ASCII) : ")
        _enc = self.encrypt(self.hashing(password, self.salt), self.iv, message)
        
        return _enc
        
    def Example_dec(self, enc_data):
        password = input("Password (ASCII) : ")
        
        return self.decrypt(self.hashing(password, self.salt), self.iv, enc_data)
    


print('''
    Consuming your Class
    
    -> Instatiate class <MyAES> and reuse your functions
    -> You can always override and inherit the methods by using, for example:
         
         def MyEncriptation(self, **myParameters):
             # ... your code here
             super(MyAES, self).encrypt(*args, **kargs)''')


SampleAES = MyAES()

# Encrypting
Enc = SampleAES.Example_enc()
if Enc:
    print("Enc: ", Enc.hex())
else:
    sys.exit()

# Decrypting
Dec = SampleAES.Example_dec(Enc)
if Dec:
    print(Dec.decode('ascii'))
