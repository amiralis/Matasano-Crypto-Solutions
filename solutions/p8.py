__author__ = 'Amirali Sanatinia'


def chunks(cipher, size):
	""" Return the splits of a text using a specified block size """
	return [cipher[i*size:(i+1)*size] for i in range(len(cipher)/size)]


def distinct_blocks(cipher, size):
	""" return the distinct blocks of size in a text """
	dist_chucnks = {}
	for chunk in chunks(cipher, size):
		dist_chucnks[chunk] = 1
	return dist_chucnks


if __name__ == '__main__':
	ciphers = open('8.txt').readlines()
	for cipher in ciphers:
		cipher = cipher.strip()
		if len(distinct_blocks(cipher, 16)) < len(cipher)/16:
			print cipher