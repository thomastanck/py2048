import random

class Dir:
	class Up: pass
	class Down: pass
	class Left: pass
	class Right: pass

class Game:
	def __init__(self):
		self.state = [[0]*4]*4
	
	def move(self, dir):
		""" Performs a move (dir should be Dir.Up, Dir.Down, etc.) """
		raise NotImplementedError()

	def display(self):
		"""
		Prints the state of the board to the display
		
		0 is blank,
		n where n in 0..9, A..Z is 2^n
		
		e.g.
		
		B 2 1 1
		1 2 0 0
		0 0 1 0
		0 0 0 0
		"""
		raise NotImplementedError()

def main():
	"""
	Handles the input and shit,
	performing the moves on
	a Game instance and displaying
	the result.
	"""
	pass

if __name__ == "__main__":
	main()
