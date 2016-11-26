import curses

from py2048 import Game, Direction

def playingmode(stdscr):
	curses.curs_set(False)
	stdscr.clear()

	game = Game()
	game.generate_random()
	game.displaycurses(stdscr)
	while True:
		ch = stdscr.getch()
		stdscr.clear()
		# stdscr.addstr(5, 0, str(ch))
		if ch == curses.KEY_UP:
			direction = Direction.Up
		elif ch == curses.KEY_DOWN:
			direction = Direction.Down
		elif ch == curses.KEY_LEFT:
			direction = Direction.Left
		elif ch == curses.KEY_RIGHT:
			direction = Direction.Right
		elif ch == ord('q'):
			break
		else:
			stdscr.addstr(5, 0, "Quit? Press q to quit")
			game.displaycurses(stdscr)
			continue
		stdscr.addstr(5, 0, direction.__name__)
		stdscr.addstr(5, 10, str(ch))
		changed = game.move(direction)
		stdscr.addstr(6, 0, str(changed))
		if changed:
			game.generate_random()
		gooddirs = []
		for d in Direction.dirs:
			if game.move(d, drymove=True):
				gooddirs.append(d.__name__)
		stdscr.addstr(7, 0, str(gooddirs))
		game.displaycurses(stdscr)

if __name__ == "__main__":
	curses.wrapper(playingmode)
