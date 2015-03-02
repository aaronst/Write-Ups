# Haymarket

Monty Hall wrote a script of how he was supposed to run one of his game shows for his trusty accounting computer some time ago, but hes not really sure what the punch cards mean any more. I mean, that was a while ago. Only, hes sure his key is hidden somewhere in these punch-cards, if he could figure out how to run them... : 150

http://bostonkeyparty.net/haymarket.tar.gz.fe35f59bfa869a0555e9972efa3ddd2d

This challenge involved reversing punched cards in order to read the program and get the flag.  The following URL was super helpful:
	- http://www.kloth.net/services/cardpunch.php
To solve it, I wrote a python script, haymarket.py, which takes a punched card image and outputs the correct characters to a file.

Extracting the given file results in a directory which contained 32 PNG images of punched cards.  Because all of the images followed a strict layout, the exact coordinates of every column and row could be calculated manually with image editting software such as GIMP. Also, the exact RGB values of a "punch" was obtained, which laid the ground-work to write a small image recognition script for this challenge.  Using the URL from above, I was able to see the entire character set and each character's corresponding punch pattern.  I hard-coded this information into my script using lists, and then let it iterate over every column on the punched card.  For every column, my script determines which rows are "punched" by looking at the R(ed) value, and stores the indeces of those rows in a temporary list.  After it has gone over every row, it performs a look-up in my list of punch patters to figure out what character it just read.  Once the character is found, it adds it to a string and moves on to the next column.  My script does this for every row, and then appends the resulting string to a text file, haymarket.txt.  Finding the flag was just a matter of reading the text file after running the script on every image.

Flag = "ALEXTREBEKISASOCIALENGINEER"
