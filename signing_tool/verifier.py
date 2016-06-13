"""This module provides a utility to verfiy digital signatures."""

from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA


def read_file(filename):
    """Get the filename and return hash of the content of the file."""
    with open(filename) as file_handle:
        data = file_handle.read()
        return data


def verify_signature(signature, hash_of_file, public_key):
    """Sign the hash of file with the key."""
    verifier = pss.new(public_key)
    try:
        verifier.verify(hash_of_file, signature)
        print "The signature is authentic."
    except (ValueError, TypeError):
        print "The signature is not authentic."


def main():
    """Main function."""
    signed_file = raw_input("Please enter the file that was signed:")
    content_of_file = read_file(signed_file)
    hash_of_file = SHA256.new(content_of_file)
    public_key_file = raw_input("\nPlease enter the file containing the public key corresponding to private key that signed the file:")
    public_key = RSA.importKey(open(public_key_file).read())
    signature_filename = raw_input("Please provide the file that contains the signature:")
    signature = read_file(signature_filename)
    verify_signature(signature, hash_of_file, public_key)

if __name__ == "__main__":
    main()
