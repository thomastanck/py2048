import curses

from py2048 import State, Direction

def playingmode(stdscr):
	curses.curs_set(False)
	stdscr.clear()

	state = State()
	state = state.generate_random()
	state.displaycurses(stdscr)
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
			state.displaycurses(stdscr)
			continue
		stdscr.addstr(5, 0, direction.__name__)
		stdscr.addstr(5, 10, str(ch))
		newstate = state.execute(direction)
		changed = state.board != newstate.board
		stdscr.addstr(6, 0, str(changed))
		if changed:
			state = newstate.generate_random()
		gooddirs = []
		for d in Direction.dirs:
			if state.execute(d).board != state.board:
				gooddirs.append(d.__name__)
		stdscr.addstr(7, 0, str(gooddirs))
		state.displaycurses(stdscr)
		stdscr.refresh()

if __name__ == "__main__":
	curses.wrapper(playingmode)
