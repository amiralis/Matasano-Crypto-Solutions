__author__ = 'Amirali Sanatinia'


def pkcs_7(plaintext, block_size):
	""" Return the PKCS#7 padded text of size block_size """
	if len(plaintext) % block_size == 0:
		padding_len = block_size
	else:
		padding_len = block_size - len(plaintext) % block_size
	padding = ('P' * padding_len).replace('P', chr(padding_len))
	return plaintext + padding

if __name__ == '__main__':
	plain_text = "YELLOW SUBMARINE"
	output = "YELLOW SUBMARINE\x04\x04\x04\x04"
	print pkcs_7(plain_text, 20) == output