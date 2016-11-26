import random
import sys
import copy

from py2048.play import playingmode
from py2048.test import testingmode
from py2048.randomtest import randommode
from py2048.randomsample import randomsamplemode

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
