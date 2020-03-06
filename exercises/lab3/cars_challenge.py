from __future__ import print_function  
import Crypto.Cipher.AES as AES
import hashlib
import binascii

car = b"<A_WELL_KNOWN_CAR_BRAND_GOES_HERE>"
sec = hashlib.sha256((car + '<REVERSED_CAR_BRAND_NAME_GOES_HERE>'  + b'JCT2020')).digest()
cipher = AES.new(sec, AES.MODE_ECB)
message = b'<SECRET_MESSAGE_GOES_HERE>'
secret = binascii.hexlify(cipher.encrypt(message))
print("Encrypted message is %s" % secret)

