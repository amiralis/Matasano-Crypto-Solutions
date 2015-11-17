__author__ = 'Amirali Sanatinia'

import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


def aes_dec_ecb(key, cipher_text):
	""" Decrypt a cipher using AES ECB """
	backend = default_backend()
	key = key
	cipher = Cipher(algorithms.AES(key), modes.ECB(), backend)
	decryptor = cipher.decryptor()
	return decryptor.update(cipher_text) + decryptor.finalize()


if __name__ == '__main__':
	cipher_text = open('7.txt').read().replace('\n', '')
	print aes_dec_ecb("YELLOW SUBMARINE", base64.b64decode(cipher_text))