import random
import sys
import copy

from play import playingmode
from test import testingmode
from randomtest import randommode
from randomsample import randomsamplemode

def main():
	"""
	Handles the input and shit,
	performing the moves on
	a Game instance and displaying
	the result.
	"""
	if len(sys.argv) == 1:
		import curses
		curses.wrapper(playingmode)
	elif sys.argv[1] == 't':
		testingmode()
	elif sys.argv[1] == 'r':
		import curses
		curses.wrapper(randommode)
	else:
		randomsamplemode(int(sys.argv[1]))

if __name__ == "__main__":
	main()
