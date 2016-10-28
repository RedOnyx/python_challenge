#!/usr/bin/python3
"""
Website url http://www.pythonchallenge.com/

Puzzle 01 url: http://www.pythonchallenge.com/pc/def/0.html

Calulate 2 to the power of 38
"""

def calc_2pow38():
	return pow(2, 38)

if __name__ == "__main__":
	num = calc_2pow38()
	print("Challenge: evaluate 2 to the power of 38.\nAnswer: {}".format(num))
	print("Next challenge url: http://www.pythonchallenge.com/pc/def/{}.html".format(num))

