from __future__ import print_function  
import Crypto.Cipher.AES as AES
import hashlib

car = "<A_WELL_KNOWN_CAR_BRAND_GOES_HERE>"
sec = hashlib.sha256(car  + '<REVERSED_CAR_BRAND_NAME_GOES_HERE>' + 'MachonLev2019').digest()
cipher = AES.new(sec, AES.MODE_ECB)
message = '<SECRET_MESSAGE_GOES_HERE>'
secret = cipher.encrypt(message).encode("hex")
print("Encrypted message is %s" % secret)

#Encrypted message is 8db0e444db0cac26e4c5762e88ba5e05b6cc12ee3a51720c296c0ccfb098bb61
