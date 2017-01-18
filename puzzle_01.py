#!/usr/bin/env python3.6
"""
Python Challenge puzzle 01
Url: http://www.pythonchallenge.com/pc/def/map.html

Clues
K -> M
O -> Q
E -> G
"""

encoded_message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
# hint ord('m') - ord('k')
# chr(97) = 'a'

def decode_message(input):
	
	message = input
	var = ord('m') - ord('k')
	output = ''
	exceptions = [' ','\'', '.', '(', ')' ]
	for character in message:
		if character in exceptions:
			output += character
		elif character == 'z':
			output += 'b'
		elif character == 'y':
			output += 'a'
		else:
			new_char = chr(ord(character)+var)
			output += new_char
	return output

if __name__ == "__main__":
	print(decode_message(encoded_message))
	print("http://www.pythonchallenge.com/pc/def/{}.html".format(decode_message('map')))
