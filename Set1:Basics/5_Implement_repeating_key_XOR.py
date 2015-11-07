__author__ = 'Amirali Sanatinia'

import binascii
import array


def rk_XOR(text, key):
	""" Encrypt text using repeating key XOR """
	text_ar = array.array('B', text)
	key_arr = array.array('B', key)
	result = array.array('B')
	for i, c in zip(xrange(len(text_ar)), text_ar):
		result.append(c ^ key_arr[i % 3])
	return result


if __name__ == '__main__':
	text = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"""
	cipher_text = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a262263242727652"\
			"72a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

	rk_xor_cipher = rk_XOR(text, 'ICE').tostring()
	assert binascii.hexlify(rk_xor_cipher) == cipher_text