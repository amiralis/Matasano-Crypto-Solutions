__author__ = 'Amirali Sanatinia'

import binascii
import array
from collections import defaultdict

from p3 import hex_to_bin
from p3 import fixed_xor_char
from p3 import score


if __name__ == '__main__':
	# read all cipher texts to memory
	cipher_texts = []
	for cipher_text in open('4.txt'):
		cipher_texts.append(cipher_text.strip())

	# find all potential texts
	potential_texts = []
	for cipher_text in cipher_texts:
		for i in range(256):
			potential_texts.append(fixed_xor_char(hex_to_bin(cipher_text), i))

	# find the score of all potential texts        
	scores = []
	for potential_text in potential_texts:
		scores.append(score(potential_text))

	# find the element with the highest score
	index = scores.index(max(scores))
	print potential_texts[index]