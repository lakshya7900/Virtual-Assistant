import time
import pyotp
import qrcode
import json


with  open('D:\Virtual Assistant\Database\key.json', 'r') as f:
        key = json.load(f)['key']\
        

def Verify(code):
    global key

    totp = pyotp.TOTP(key)
    return totp.verify(code)

def Connect():
    global key

    uri = pyotp.totp.TOTP(key).provisioning_uri(
        name='Virtual Assistant',
        issuer_name='lakshya7900')
    
    print(uri)
    qrcode.make(uri).save("D:\Virtual Assistant\Database\qr.png")    

def GenerateKey():
    k = pyotp.random_base32()
    dict = {'key': k}
    with open('D:\Virtual Assistant\Database\key.json', 'w') as file:
        json.dump(dict, file)

Connect()
