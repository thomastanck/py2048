import random

from py2048.game import Game, Direction

def randomsamplemode(numtogenerate):
	game = Game()
	# for i in range(numtogenerate):
	#	game.generate_random()
	game.generate(0, 0, 2)
	game.generate(0, 1, 1)
	game.generate(0, 2, 0)
	game.generate(0, 3, 0)
	print("Initial state")
	game.display()
	print()
	direction = random.choice(Direction.dirs)
	direction = Direction.Left
	print("Doing the calculations when moving", direction.__name__)
	game.move(direction, debugprint=True)
	print()
	print("After moving", direction.__name__)
	game.display()
	print()
