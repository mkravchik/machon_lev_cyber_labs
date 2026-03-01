from __future__ import print_function  
import Crypto.Cipher.AES as AES
import hashlib
import binascii

name = b"<A_NAME_OF_SOME_MITRE_CAMPAIGN_GOES_HERE>"
sec = hashlib.sha512((name + REVERSED_MITRE_CAMPAIGN_GOES_HERE + b'2026')).digest()
cipher = AES.new(sec[USE_FIRST_32_BYTES], AES.MODE_ECB)

# notice - the message' length is divisible by 16
message = b'<SECRET_MESSAGE_GOES_HERE>'
secret = binascii.hexlify(cipher.encrypt(message))
print("Encrypted message is %s" % secret)
