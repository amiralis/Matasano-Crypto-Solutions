__author__ = 'Amirali Sanatinia'

import binascii
import array
from collections import defaultdict


def hex_to_bin(hex_input):
	""" Convert hex to binary """
	return binascii.unhexlify(hex_input)


def fixed_xor_char(bin_val1, char):
	""" Fixed XOR of a string and a character(int) """
	output = array.array('B')
	# convert two strings into a byte array
	a1 = array.array('B', bin_val1)
	for i in a1:
		output.append(i ^ char)
	return output.tostring()


def score(text):
	""" Get the score of a text using the letter frequencies, including space """
	freqs = {
	'a' : 8.167,
	'b' : 1.492,
	'c' : 2.782,
	'd' : 4.253,
	'e' : 12.702, 
	'f' : 2.228,
	'g' : 2.015,
	'h' : 6.094,
	'i' : 6.966,
	'j' : 0.153,
	'k' : 0.772,
	'l' : 4.025,
	'm' : 2.406,
	'n' : 6.749,
	'o' : 7.507,
	'p' : 1.929,
	'q' : 0.095,
	'r' : 5.987,
	's' : 6.327,
	't' : 9.056,
	'u' : 2.758,
	'v' : 0.978,
	'w' : 2.361,
	'x' : 0.150,
	'y' : 1.974, 
	'z' : 0.074,
	' ' : 19.519}
	freqs = defaultdict(int, freqs)
	text_score = 0
	for c in text:
		text_score += freqs[c]
	return text_score


if __name__ =='__main__':
	cipher_text = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
	potential_texts = []
	for i in range(256):
		potential_texts.append(fixed_xor_char(hex_to_bin(cipher_text), i))
	scores = []
	for potential_text in potential_texts:
		scores.append(score(potential_text))

	# find the element with the highest score
	index = scores.index(max(scores))
	print potential_texts[index]