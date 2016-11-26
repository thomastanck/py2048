import copy

from py2048.game import Game, Direction

def testingmode():
	game = Game()
	numfailed = 0
	for start, direction, supposedtochange, finish in tests:
		game.state = copy.deepcopy(start)
		changed = game.move(direction)
		# print(changed, supposedtochange, game.state, finish)
		if changed != supposedtochange or game.state != finish:
			printfailedtest(start, direction, supposedtochange, finish, changed, game)
			numfailed += 1
	print('{}/{} tests failed'.format(numfailed, len(tests)))

def printfailedtest(start, direction, supposedtochange, finish, changed, game):
	tempgame = Game()
	print('============')
	print('Failed test:')
	print('============')
	print('Start:')
	tempgame.state = copy.deepcopy(start)
	tempgame.display()
	print('Direction:', direction.__name__)
	print('Changed:', changed)
	print('Finish:')
	game.display()
	print('Expected changed:', supposedtochange)
	print('Expected finish:')
	tempgame.state = copy.deepcopy(finish)
	tempgame.display()
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