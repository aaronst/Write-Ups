#!/usr/bin/python

# Boston Key Party CTF 2015
# Haymarket
#
# Author:  aaronst
#
# This script reads in a PNG image of a punched card and outputs the correct characters to
# a text file.
#
# Usage:  $ ./haymarket.py <punched_card.png>

import Image
import sys

if (len(sys.argv) != 2):
	print 'Usage:  ' + sys.argv[0] + ' <punched_card.png>'

image = Image.open(sys.argv[1])

# Punched card layout values.  Determined by opening up one of the given images in GIMP.
column_width = 7
column_height = 20
first_column_x = 15
first_column_y = 20
punch_color = 20

# List of the character set for the punched cards.
chars = ['&', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C',
		'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
		'/', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ':', '#', '@', '\'', '=', '\"',
		'[', '.', '<', '(', '+', '^', '!', '$', '*', ')', ';', '\\', ']', ',', '%',
		'_', '>', '?']

# List of the punch patterns corresponding (by index) to the characters in the chars list.  Each number
# represents the index of a "punched" row, with 0 being the top row and 11 being the bottom.  These
# patterns were determined using the punched card emulator at http://www.kloth.net/services/cardpunch.php.
patterns = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [0, 3], [0, 4],
			[0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [1, 3], [1, 4], [1, 5],
			[1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [1, 11], [2, 3], [2, 4], [2, 5], [2, 6],
			[2, 7], [2, 8], [2, 9], [2, 10], [2, 11], [4, 10], [5, 10], [6, 10], [7, 10],
			[8, 10], [9, 10], [0, 4, 10], [0, 5, 10], [0, 6, 10], [0, 7, 10], [0, 8, 10],
			[0, 9, 10], [1, 4, 10], [1, 5, 10], [1, 6, 10], [1, 7, 10], [1, 8, 10], [1, 9, 10],
			[2, 4, 10], [2, 5, 10], [2, 6, 10], [2, 7, 10], [2, 8, 10], [2, 9, 10]]

# Initial string for output.
text = ""

# For every column on the punched card...
for i in range (0, 80):
	
	# Initial pattern list.
	pattern = []
	
	# For every row in the current column...
	for j in range (0, 12):

		# If the current row is "punched"...
		if (image.getpixel((first_column_x + (i * column_width),
			first_column_y + (j * column_height)))[0] == punch_color):
			
			# Record the index in our pattern list.
			pattern.append(j)

	# Ignore empty columns.
	if (pattern != []):
		
		# Record the character that corresponds with the resulting pattern.
		text += chars[patterns.index(pattern)]

# Output the resulting string to console.
print text

# Write the string to a file.
out = open('haymarket.txt', 'a')
out.write(text)
