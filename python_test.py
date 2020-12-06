#!/usr/bin/env python

import sys
import os
import re
import ast
import argparse
import getpass
import datetime


def print_welcome():
	date = datetime.datetime.now().strftime("%B %d %Y")
	print(f"Hello, {getpass.getuser()}! Today is {date}. Beautiful day for miracles!") 

def main():
	filename = 'string.txt'
	with open(filename) as file_object:
		contents = file_object.read()
	elements = ast.literal_eval(contents)
	print_welcome()	
	print("Input string:\n", contents.rstrip())
	print("Output tuples:")
	tuples_union = []
	numbers = []
	for element in elements:
		if isinstance(element, tuple):
			for t in element:
				tuples_union.append(t)
		else:
			numbers.append(element)
	for number in numbers:
		if len(tuples_union) >=  number:
			print(tuple(tuples_union[:number]))
			del tuples_union[:number]
	
				





#	print(contents.rstrip())
#	match = re.search(r"\(.*?\)", contents)
#	tuples = re.findall(r"\(.*?\)", contents)
#	truncated = re.sub(r"\(.*?\)", '', contents)
#	print('result after delete', truncated)
#	t = tuple(truncated)
#	print('tupled', t)
#	s = ast.literal_eval(contents)
#	print(s)
	

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description = 'Magical pipeline.')
	parser.add_argument('-f', '--file', help='input file')
	parser.add_argument('-o', '--out', help='output file')
#	parser.add_argument('-o', '--out', help='output file')
	args = parser.parse_args()
	main()
