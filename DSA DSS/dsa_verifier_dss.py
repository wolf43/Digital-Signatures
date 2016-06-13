"""This module verifies a signature signed using DSS standard."""

from Crypto.Signature import DSS
from Crypto.Hash import SHA256
from Crypto.PublicKey import DSA

message = 'To be signed'

key = DSA.importKey(open('pubkey.bin').read())
h = SHA256.new(message)
verifier = DSS.new(key, 'fips-186-3')
f = open("signature.bin", "rb")
signature = f.read()
try:
    verifier.verify(h, signature)
    print "The signature is authentic."
except (ValueError, TypeError):
    print "The signature is not authentic."
