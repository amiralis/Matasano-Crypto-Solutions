__author__ = 'Amirali Sanatinia'


import random
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
backend = default_backend()

from p2 import fixed_xor
from p8 import chunks
from p9 import pkcs_7


def aes_enc_ecb(msg, key):
	""" Encrypt a message of size 128 bits (16 bytes) using AES ECB """
	cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
	encryptor = cipher.encryptor()
	ct = encryptor.update(msg) + encryptor.finalize()
	return ct


def aes_enc_cbc(msg, iv, key):
	""" Encrypt a message of size 128 bits (16 bytes) using AES CBC """
	blocks = []
	for block in chunks(msg, 16):
		_msg = fixed_xor(iv,  block).tostring()
		_ct_block = aes_enc_ecb(_msg, key)
		blocks.append(_ct_block)
		iv = _ct_block
	return "".join(blocks)


def test_CBC(msg, iv, key):
	""" Encrypt a message of size 128 bits (16 bytes) using AES CBC (the cryptography library implementation for testing"""
	cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
	encryptor = cipher.encryptor()
	ct = encryptor.update(msg) + encryptor.finalize()
	return ct


if __name__ == '__main__':
	for _ in range(200):
		msg = os.urandom(random.randint(1, 1000))
		key = os.urandom(16)
		iv = os.urandom(16)
		assert test_CBC(pkcs_7(msg, 16), iv, key) == aes_enc_cbc(pkcs_7(msg, 16), iv, key)