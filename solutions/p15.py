__author__ = 'Amirali Sanatinia'


from p9 import pkcs_7


def verify_pkcs7(msg, size=16):
	""" Verify the PKCS#7 and return the stripped message if it is proper """

	if len(msg) % size != 0:
		raise ValueError("Bad Padding")
	
	padding_c = msg[-1]
	pad_len = ord(msg[-1])
	padding = msg[-(pad_len):]
	for c in padding:
		if c != padding_c:
			raise ValueError("Bad Padding")
	return msg[:-(pad_len)]


if __name__ == '__main__':
	assert verify_pkcs7("ICE ICE BABY\x04\x04\x04\x04") == "ICE ICE BABY"
	
	try:
		verify_pkcs7("ICE ICE BABY\x05\x05\x05\x05")
	except ValueError, e:
		assert str(e) == 'Bad Padding'

	try:
		verify_pkcs7("ICE ICE BABY\x01\x02\x03\x04")
	except ValueError, e:
		assert str(e) == 'Bad Padding'