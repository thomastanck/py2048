import copy

from py2048 import State, Direction

def testingmode():
	state = State()
	numfailed = 0
	for start, direction, supposedtochange, finish in tests:
		start = [*start[0], *start[1], *start[2], *start[3]]
		finish = [*finish[0], *finish[1], *finish[2], *finish[3]]

		state.board = start[:]
		newstate = state.execute(direction)

		changed = state.board != newstate.board

		if changed != supposedtochange or newstate.board != finish:
			printfailedtest(start, direction, supposedtochange, finish, changed, state, newstate)
			numfailed += 1

	print('{}/{} tests failed'.format(numfailed, len(tests)))

def printfailedtest(start, direction, supposedtochange, finish, changed, state, newstate):
	print('============')
	print('Failed test:')
	print('============')
	print('Start:')
	state.display()
	print('Direction:', direction.__name__)
	print('Changed:', changed)
	print('Finish:')
	newstate.display()
	print('Expected changed:', supposedtochange)
	print('Expected finish:')
	tempstate = State()
	tempstate.board = copy.deepcopy(finish)
	tempstate.display()
	print()


tests = [
	# Null test
	(
		[
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		],
		Direction.Up,
		False,
		[
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		]
	),
	# Testing merging behaviour
	(
		[
			[1, 0, 0, 0],
			[1, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		],
		Direction.Up,
		True,
		[
			[2, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		]
	),
	(
		[
			[1, 0, 0, 0],
			[1, 0, 0, 0],
			[1, 0, 0, 0],
			[0, 0, 0, 0]
		],
		Direction.Up,
		True,
		[
			[2, 0, 0, 0],
			[1, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		]
	),
	# Only one merge per cell per move
	(
		[
			[1, 0, 0, 0],
			[1, 0, 0, 0],
			[1, 0, 0, 0],
			[1, 0, 0, 0]
		],
		Direction.Up,
		True,
		[
			[2, 0, 0, 0],
			[2, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		]
	),
	(
		[
			[1, 0, 0, 0],
			[1, 0, 0, 0],
			[2, 0, 0, 0],
			[0, 0, 0, 0]
		],
		Direction.Up,
		True,
		[
			[2, 0, 0, 0],
			[2, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		]
	),
	(
		[
			[1, 0, 0, 0],
			[1, 0, 0, 0],
			[2, 0, 0, 0],
			[2, 0, 0, 0]
		],
		Direction.Up,
		True,
		[
			[2, 0, 0, 0],
			[3, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		]
	),
	# Traversal over empty cells
	(
		[
			[0, 0, 0, 0],
			[1, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		],
		Direction.Up,
		True,
		[
			[1, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		]
	),
	(
		[
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[1, 0, 0, 0],
			[0, 0, 0, 0]
		],
		Direction.Up,
		True,
		[
			[1, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		]
	),
	(
		[
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[1, 0, 0, 0]
		],
		Direction.Up,
		True,
		[
			[1, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		]
	),
	(
		[
			[1, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[1, 0, 0, 0]
		],
		Direction.Up,
		True,
		[
			[2, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		]
	),
	(
		[
			[0, 0, 0, 0],
			[1, 0, 0, 0],
			[0, 0, 0, 0],
			[1, 0, 0, 0]
		],
		Direction.Up,
		True,
		[
			[2, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		]
	),
	(
		[
			[2, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[1, 0, 0, 0]
		],
		Direction.Up,
		True,
		[
			[2, 0, 0, 0],
			[1, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		]
	),
	(
		[
			[0, 0, 0, 0],
			[2, 0, 0, 0],
			[0, 0, 0, 0],
			[1, 0, 0, 0]
		],
		Direction.Up,
		True,
		[
			[2, 0, 0, 0],
			[1, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		]
	),
	(
		[
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[2, 0, 0, 0],
			[1, 0, 0, 0]
		],
		Direction.Up,
		True,
		[
			[2, 0, 0, 0],
			[1, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		]
	),
	# Traversal over empty cells (last column duplicate)
	(
		[
			[0, 0, 0, 0],
			[0, 0, 0, 1],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		],
		Direction.Up,
		True,
		[
			[0, 0, 0, 1],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		]
	),
	(
		[
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 1],
			[0, 0, 0, 0]
		],
		Direction.Up,
		True,
		[
			[0, 0, 0, 1],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		]
	),
	(
		[
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 1]
		],
		Direction.Up,
		True,
		[
			[0, 0, 0, 1],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		]
	),
	(
		[
			[0, 0, 0, 1],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 1]
		],
		Direction.Up,
		True,
		[
			[0, 0, 0, 2],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		]
	),
	(
		[
			[0, 0, 0, 0],
			[0, 0, 0, 1],
			[0, 0, 0, 0],
			[0, 0, 0, 1]
		],
		Direction.Up,
		True,
		[
			[0, 0, 0, 2],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		]
	),
	(
		[
			[0, 0, 0, 2],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 1]
		],
		Direction.Up,
		True,
		[
			[0, 0, 0, 2],
			[0, 0, 0, 1],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		]
	),
	(
		[
			[0, 0, 0, 0],
			[0, 0, 0, 2],
			[0, 0, 0, 0],
			[0, 0, 0, 1]
		],
		Direction.Up,
		True,
		[
			[0, 0, 0, 2],
			[0, 0, 0, 1],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		]
	),
	(
		[
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 2],
			[0, 0, 0, 1]
		],
		Direction.Up,
		True,
		[
			[0, 0, 0, 2],
			[0, 0, 0, 1],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		]
	),
	# Blocking
	(
		[
			[2, 0, 0, 0],
			[1, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		],
		Direction.Up,
		False,
		[
			[2, 0, 0, 0],
			[1, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		]
	),
	(
		[
			[1, 0, 0, 0],
			[2, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		],
		Direction.Up,
		False,
		[
			[1, 0, 0, 0],
			[2, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		]
	),
	(
		[
			[1, 0, 0, 0],
			[2, 0, 0, 0],
			[1, 0, 0, 0],
			[0, 0, 0, 0]
		],
		Direction.Up,
		False,
		[
			[1, 0, 0, 0],
			[2, 0, 0, 0],
			[1, 0, 0, 0],
			[0, 0, 0, 0]
		]
	),
	(
		[
			[2, 0, 0, 0],
			[1, 0, 0, 0],
			[0, 0, 0, 0],
			[2, 0, 0, 0]
		],
		Direction.Up,
		True,
		[
			[2, 0, 0, 0],
			[1, 0, 0, 0],
			[2, 0, 0, 0],
			[0, 0, 0, 0]
		]
	),
	# Making sure the other directions even do stuff
	(
		[
			[1, 1, 1, 1],
			[1, 0, 0, 0],
			[1, 0, 0, 0],
			[1, 0, 0, 0]
		],
		Direction.Up,
		True,
		[
			[2, 1, 1, 1],
			[2, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		]
	),
	(
		[
			[1, 1, 1, 1],
			[1, 0, 0, 0],
			[1, 0, 0, 0],
			[1, 0, 0, 0]
		],
		Direction.Down,
		True,
		[
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[2, 0, 0, 0],
			[2, 1, 1, 1]
		]
	),
	(
		[
			[1, 1, 1, 1],
			[1, 0, 0, 0],
			[1, 0, 0, 0],
			[1, 0, 0, 0]
		],
		Direction.Left,
		True,
		[
			[2, 2, 0, 0],
			[1, 0, 0, 0],
			[1, 0, 0, 0],
			[1, 0, 0, 0]
		]
	),
	(
		[
			[1, 1, 1, 1],
			[1, 0, 0, 0],
			[1, 0, 0, 0],
			[1, 0, 0, 0]
		],
		Direction.Right,
		True,
		[
			[0, 0, 2, 2],
			[0, 0, 0, 1],
			[0, 0, 0, 1],
			[0, 0, 0, 1]
		]
	),
]

if __name__ == "__main__":
	testingmode()
