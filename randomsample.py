import random

from py2048 import State, Direction

def randomsamplemode(numtogenerate):
	state = State()
	for i in range(numtogenerate):
		state = state.generate_random()
	# state.generate(0, 0, 2)
	# state.generate(0, 1, 1)
	# state.generate(0, 2, 0)
	# state.generate(0, 3, 0)
	print("Initial state")
	state.display()
	print()
	direction = random.choice(Direction.dirs)
	# direction = Direction.Left
	state = state.execute(direction)
	print("After moving", direction.__name__)
	state.display()
	print()

if __name__ == "__main__":
	numtogenerate = int(sys.argv[1])
	randomsamplemode(numtogenerate)
