import curses
import random

from py2048 import State, Direction

def randommode(stdscr):
	curses.curs_set(False)
	stdscr.clear()

	state = State().generate_random()
	state.displaycurses(stdscr)

	gooddirs = set(Direction.dirs)
	while True:
		if len(gooddirs) == 0:
			ch = stdscr.getch()
			if ch == ord('q'):
				break
			state = State().generate_random()
			gooddirs = set(Direction.dirs)
		direction = random.choice(list(gooddirs))
		stdscr.clear()
		stdscr.addstr(5, 0, direction.__name__)
		newstate = state.execute(direction)
		changed = state.board != newstate.board
		stdscr.addstr(6, 0, str(changed))
		if changed:
			state = newstate.generate_random()
			gooddirs = set(Direction.dirs)
		else:
			gooddirs.remove(direction)
		state.displaycurses(stdscr)
		stdscr.refresh()

if __name__ == "__main__":
	curses.wrapper(randommode)
