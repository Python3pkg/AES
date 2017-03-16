# AES
AES Cryptography in Python

## Installing
1. Check if Python 3+ is installed
2. ```pip install PySimpleAES``` 


## How it works

### Available Functions
Check the table below for available methods in this module

Method         | Objective                     | Return
---------------|-------------------------------|---------------
fortify() | Savorless code, never more! | str: iv, str: salt
hashing(password, salt) | Hash the message | str: key
encrypt(key, iv, msg) | Encrypt a message | str: Encrypted message
decrypt(key, iv, password) | Decrypt the message | str: Decrypted message


### Example code
You can find a sample of usage on the **examples.py**. But to save your time, let's see how it works:
```python
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
```

## Tests
* Tested on Python 3.6 32 bits
* Tested on Windows 10 x64
