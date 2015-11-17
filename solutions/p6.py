__author__ = 'Amirali Sanatinia'

import array


def hamming_dist(text1, text2):
	""" Find the edit/hamming distance between to strings """
	diff = 0
	for i, j in zip(text1, text2):
		if i != j:
			diff += 1
	return diff

def str_2_bin(text):
	""" Convert string text to a binary number """
	str_a = array.array('B', text)
	binary = []
	for c in str_a:
		b = bin(c).replace('0b','')
		# padding to 8 bit
		if len(b) < 8:
			b = '0'*(8-len(b)) + b  
		binary.append(b)

	return ''.join(binary)


if __name__ == '__main__':

	s1 = "this is a test"
	s2 = "wokka wokka!!!"

	# check str_2_bin and hamming dist func
	assert hamming_dist(str_2_bin(s1), str_2_bin(s2)) == 37