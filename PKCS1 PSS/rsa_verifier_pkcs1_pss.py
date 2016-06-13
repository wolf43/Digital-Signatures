"""This module verifies a signature signed using PKCS1 PSS standard."""

from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
# from Crypto import Random

message = 'To be signed'

key = RSA.importKey(open('pubkey.bin').read())
h = SHA256.new(message)
verifier = pss.new(key)
f = open("signature.bin", "rb")
signature = f.read()
try:
    verifier.verify(h, signature)
    print "The signature is authentic."
except (ValueError, TypeError):
    print "The signature is not authentic."
