__author__ = 'Amirali Sanatinia'

import binascii
import base64


def hex_to_bin(hex_input):
	""" Convert hex to binary """
	return binascii.unhexlify(hex_input)

def bin_to_b64(bin_input):
	""" Convert binary to base64 """
	return base64.b64encode(bin_input)

if __name__ == '__main__':
	test_hex="""49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"""
	test_b64="""SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"""

	assert bin_to_b64(hex_to_bin(test_hex)) == test_b64