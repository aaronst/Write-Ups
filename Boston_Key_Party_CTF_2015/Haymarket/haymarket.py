#!/usr/bin/python

import Image
import sys

if (len(sys.argv) != 2):
	print 'Usage:  ' + sys.argv[0] + ' <punched_card.png>'

image = Image.open(sys.argv[1])

column_width = 7
column_height = 20
first_column_x = 15
first_column_y = 20
punch_color = 20

chars = ['&', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C',
		'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
		'/', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ':', '#', '@', '\'', '=', '\"',
		'[', '.', '<', '(', '+', '^', '!', '$', '*', ')', ';', '\\', ']', ',', '%',
		'_', '>', '?']

patterns = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [0, 3], [0, 4],
			[0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [1, 3], [1, 4], [1, 5],
			[1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [1, 11], [2, 3], [2, 4], [2, 5], [2, 6],
			[2, 7], [2, 8], [2, 9], [2, 10], [2, 11], [4, 10], [5, 10], [6, 10], [7, 10],
			[8, 10], [9, 10], [0, 4, 10], [0, 5, 10], [0, 6, 10], [0, 7, 10], [0, 8, 10],
			[0, 9, 10], [1, 4, 10], [1, 5, 10], [1, 6, 10], [1, 7, 10], [1, 8, 10], [1, 9, 10],
			[2, 4, 10], [2, 5, 10], [2, 6, 10], [2, 7, 10], [2, 8, 10], [2, 9, 10]]

text = ""

for i in range (0, 80):
	pattern = []
	for j in range (0, 12):
		if (image.getpixel((first_column_x + (i * column_width),
			first_column_y + (j * column_height)))[0] == punch_color):
			pattern.append(j)

	if (pattern != []):
		text += chars[patterns.index(pattern)]

print text

out = open('haymarket.txt', 'a')
out.write(text)