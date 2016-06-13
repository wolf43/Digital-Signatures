"""This module generates a DSA key pair and stores it."""

from Crypto.PublicKey import DSA


key = DSA.generate(2048)
private_key = key.exportKey()

file_out = open("dsa_key.bin", "wb")
file_out.write(private_key)

pub_key = key.publickey().exportKey()
file_out = open("pubkey.bin", "wb")
file_out.write(pub_key)
