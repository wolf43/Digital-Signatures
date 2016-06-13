"""This module helps user sign a file using DSS standard."""

from Crypto.Signature import DSS
from Crypto.Hash import SHA256
from Crypto.PublicKey import DSA

message = 'To be signed'
key = DSA.importKey(open('dsa_key.bin').read())
h = SHA256.new(message)
signer = DSS.new(key, 'fips-186-3')
signature = signer.sign(h)
print signature
f = open("signature.bin", "wb")
f.write(signature)
