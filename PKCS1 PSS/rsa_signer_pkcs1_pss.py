"""This module helps user sign a file using PKCS1 PSS standard."""

from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
# from Crypto import Random

message = 'To be signed'
key = RSA.importKey(open('rsa_key.bin').read())
h = SHA256.new(message)
signature = pss.new(key).sign(h)
print signature
f = open("signature.bin", "wb")
f.write(signature)
