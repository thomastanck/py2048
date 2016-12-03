import random
import string
import copy

def displaycharfor(num):
	if num == 0:
		return '-'
	elif 1 <= num <= 9:
		return str(num)
	else:
		return string.ascii_uppercase[num-10]

class Direction:
	class Up: pass
	class Down: pass
	class Left: pass
	class Right: pass
	dirs = [Up, Down, Left, Right]

class State:
	""" Rewrite of Game in a immutable way and stuff. """
	@staticmethod
	def init_move_table():
		"""
		Initialise a table that's used to look up the outcome of a
		left move in any given row.
		"""
		# Enumerate rows
		rows = []
		for a in range(16):
			for b in range(16):
				for c in range(16):
					for d in range(16):
						rows.append([a, b, c, d])
		# Loop through rows and move left.
		# Ported from https://github.com/nneonneo/2048-ai/blob/master/2048.cpp#L153
		#out = [None] * len(rows)
		for row in rows:
			i = -1 # Mimic a C for loop... just because...
			while True:
				i += 1
				for j in range(i+1, 4):
					if row[j] != 0:
						break
				else:
					break # No more tiles on the right
				if row[i] == 0:
					row[i] = row[j] # Move!
					row[j] = 0
					i -= 1 # Retry this entry
					continue
				if row[i] == row[j]:
					row[i] += 1 # Merge!
					row[j] = 0

		return rows

	def __init__(self):
		"""
		The board state is an array. The indices are row-major
		or English reading order.
		"""
		self.board = [0]*16

	def execute(self, direction):
		"""
		Returns a State where the move is
		executed.
		"""
		out = State()
		for i in range(4):
			if direction == Direction.Up:
				row = self.board[i::4]
			elif direction == Direction.Down:
				row = self.board[i-4::-4]
			elif direction == Direction.Left:
				row = self.board[4*i:4*i+4]
			elif direction == Direction.Right:
				row = self.board[4*i+3-16:4*i-1-16:-1]
			index = 0
			for v in row:
				index *= 16
				index += v
			outrow = self._move_table[index]
			if direction == Direction.Up:
				out.board[i::4] = outrow
			elif direction == Direction.Down:
				out.board[i-4::-4] = outrow
			elif direction == Direction.Left:
				out.board[4*i:4*i+4] = outrow
			elif direction == Direction.Right:
				out.board[4*i+3-16:4*i-1-16:-1] = outrow
		return out

	def generate(self, row, col, value=1):
		assert(self.board[row*4+col] == 0)
		out = State()
		out.board = self.board[:]
		out.board[row*4+col] = value
		return out

	def generate_random(self):
		out = State()
		blanks = set()
		for i in range(16):
			if self.board[i] == 0:
				blanks.add(i)
			else:
				out.board[i] = self.board[i]
		out.board[random.choice(blanks)] = 2 if random.randrange(10) == 0 else 1
		return out

	def display(self):
		for n in range(4):
			print(' '.join(map(displaycharfor, self.board[4*n:4*n+4])))

	def displaycurses(self, stdscr):
		""" Curses version of display """
		for row in range(4):
			stdscr.addstr(row, 0, ' '.join(map(displaycharfor, self.board[4*n:4*n+4])))
		#stdscr.refresh()

State._move_table = State.init_move_table()

class Game:
	def __init__(self):
		self.state = []
		for row in range(4):
			self.state.append([])
			for col in range(4):
				self.state[row].append(0)

	def get(self, row, col, direction):
		"""
		Gets value a coordinate, but with the `direction` side of the board facing the top
		"""
		if direction == Direction.Up:
			r, c = row, col
		elif direction == Direction.Down:
			r, c = 3-row, 3-col
		elif direction == Direction.Left:
			r, c = 3-col, row
		elif direction == Direction.Right:
			r, c = col, 3-row
		return self.state[r][c]

	def set(self, row, col, direction, value):
		"""
		Sets value at a coordinate, but with the `direction` side of the board facing the top
		"""
		if direction == Direction.Up:
			r, c = row, col
		elif direction == Direction.Down:
			r, c = 3-row, 3-col
		elif direction == Direction.Left:
			r, c = 3-col, row
		elif direction == Direction.Right:
			r, c = col, 3-row
		self.state[r][c] = value

	def move(self, direction, debugprint=False, drymove=False):
		"""
		Performs a move (direction should be Direction.Up, Direction.Down, etc.)

		If debugprint is True, prints some debugging stuff.
		If drymove is True, it doesn't modify the state and just checks if a certain move is valid.

		Returns True if a change was made, returns False if no tiles changed.
		"""
		changed = False

		for col in range(4):
			merged = []
			for row in range(1, 4):
				if debugprint: print(row, col)
				if self.get(row, col, direction) != 0:
					for moveto in range(row-1, -1, -1):
						if debugprint: print('--', moveto, self.get(moveto, col, direction))
						if self.get(moveto, col, direction) == 0:
							if moveto == 0:
								changed = True
								if drymove: break
								self.set(moveto, col, direction, self.get(row, col, direction))
								self.set(row, col, direction, 0)
							continue
						elif self.get(moveto, col, direction) == self.get(row, col, direction):
							changed = True
							if drymove: break
							if moveto in merged:
								self.set(moveto+1, col, direction, self.get(row, col, direction))
								self.set(row, col, direction, 0)
								break
							merged.append(moveto)
							if debugprint: print('merged', merged)
							self.set(moveto, col, direction, self.get(moveto, col, direction) + 1)
							self.set(row, col, direction, 0)
							break
						else:
							if moveto+1 != row:
								changed = True
								if drymove: break
								self.set(moveto+1, col, direction, self.get(row, col, direction))
								self.set(row, col, direction, 0)
							break

		return changed

	def generate(self, row, col, value=1):
		""" Puts a value in a certain spot. """
		assert(0 <= row < 4)
		assert(0 <= col < 4)
		assert(self.state[row][col] == 0)
		self.state[row][col] = value

	def generate_random(self):
		emptycells = set()
		for row in range(4):
			for col in range(4):
				if self.state[row][col] == 0:
					emptycells.add((row, col))
		emptycells = list(emptycells)
		assert(len(emptycells) > 0)
		value = 1 if random.randrange(10) > 0 else 2
		row, col = random.choice(emptycells)
		self.generate(row, col, value)

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
		print('\n'.join(
				' '.join(map(displaycharfor, self.state[row]))
				for row in range(4)
			)
		)

	def displaycurses(self, stdscr):
		""" Curses version of display """
		for row in range(4):
			stdscr.addstr(row, 0, ' '.join(map(displaycharfor, self.state[row])))
		#stdscr.refresh()

	def copy(self):
		"""
		Returns a deep copy of itself.
		"""
		newgame = Game()
		newgame.state = copy.deepcopy(self.state)
		return newgame
