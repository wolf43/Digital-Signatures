"""This module provides a utility to sign files using PKCS1 PSS."""

from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA


def read_file(filename):
    """Get the filename and return hash of the content of the file."""
    with open(filename) as file_handle:
        data = file_handle.read()
        return data


def write_to_file(filename, data):
    """Write data to file."""
    file_handle = open(filename, "wb")
    file_handle.write(data)


def sign_file(key, hash_of_file):
    """Sign the hash of file with the key."""
    signature = pss.new(key).sign(hash_of_file)
    return signature


def main():
    """Main function."""
    file_to_sign = raw_input("Please enter the file to sign:")
    content_of_file = read_file(file_to_sign)
    hash_of_file = SHA256.new(content_of_file)
    private_key_file = raw_input("\nIf you don't have a file with private key, please run keygen.py\nPlease enter the file containing the private key:")
    private_key = RSA.importKey(open(private_key_file).read())
    signature = sign_file(private_key, hash_of_file)
    signature_filename = raw_input("Please provide a name for the file where signature should be stored:")
    write_to_file(signature_filename, signature)

if __name__ == "__main__":
    main()
