__author__ = 'Amirali Sanatinia'

import binascii
import array

def hex_to_bin(hex_input):
	""" Convert hex to binary """
	return binascii.unhexlify(hex_input)

def fixed_xor(bin_val1, bin_val2):
    """ Fixed XOR of two strings """
    output = array.array('B')

    # convert two strings into a byte array
    a1 = array.array('B', bin_val1)
    a2 = array.array('B', bin_val2)
    for i, j in zip(a1, a2):
    	output.append(i ^ j)
    return output

if __name__ == '__main__':
	test_s1 = '1c0111001f010100061a024b53535009181c'
	test_s2 = '686974207468652062756c6c277320657965'
	test_result = '746865206b696420646f6e277420706c6179'

	answer = fixed_xor(hex_to_bin(test_s1), hex_to_bin(test_s2))
	assert binascii.hexlify(answer.tostring()) == test_result