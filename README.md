# Digital Signatures
### Introduction
Digital signatures are a cryptographic primitive that provide authentication and integrity. In plain English, it means that when you get a signature
* Authentication: You can make sure that someone in possession of the private key signed the documents. No one without the private key can generate the signature
* Integrity: You can be sure that the file was not altered after the signature was computed on the file

### Strcuture of the project
* PKCS1 PSS: This folder contains simple code for PKCS1 PSS digital signature
* DSA DSS: This folder contains simple code for DSS digital signature
* signing_tool: This is tool that lets you sign files and verify signatures on files  
For all the projects, run:
* keygen.py
* signer.py
* verifier.py

### Dependencies
It requires Python and Pycryptodome<http://pycryptodome.readthedocs.io/en/latest/src/introduction.html>  
You can get Pycryptodome by running "pip install pycryptodome"  
You should do it in a virtual enviorment if you already have pycrypto as it is a fork of pycrypto and they might interfeare with each other in unexpted ways