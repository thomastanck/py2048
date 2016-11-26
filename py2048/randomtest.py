import curses
import random

from py2048.game import Game, Direction

def randommode(stdscr):
	curses.curs_set(False)
	stdscr.clear()

	game = Game()
	game.generate_random()
	game.displaycurses(stdscr)

	gooddirs = set(Direction.dirs)
	while True:
		if len(gooddirs) == 0:
			ch = stdscr.getch()
			if ch == ord('q'):
				break
			game = Game()
			game.generate_random()
			gooddirs = set(Direction.dirs)
		direction = random.choice(list(gooddirs))
		stdscr.clear()
		stdscr.addstr(5, 0, direction.__name__)
		changed = game.move(direction)
		stdscr.addstr(6, 0, str(changed))
		if changed:
			game.generate_random()
			gooddirs = set(Direction.dirs)
		else:
			gooddirs.remove(direction)
		game.displaycurses(stdscr)
