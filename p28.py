import time

t = time.time()

def printGrid(grid):
	for x in grid:
		print(x)

def makeGrid(size):
	if(size%2 == 0):
		return
	grid = []
	for row in range(size):
		r = []
		for col in range(size):
			r.append(0)
		grid.append(r)
	return grid	

def makeSpiral(size):
	grid = makeGrid(size)
	row = size//2
	col = size//2
	num_moves = 1
	moves_left = 1
	finished_count = 0
	# 1:right, 2:down, 3:left, 4:up
	direction = 1
	for n in range(1, size**2+1):
		grid[row][col] = n
		if(direction == 1):
			col += 1
		elif(direction == 2):
			row += 1
		elif(direction == 3):
			col -= 1
		elif(direction == 4):
			row -= 1
		moves_left -= 1
		if(moves_left == 0):
			direction = (direction%4)+1
			finished_count += 1
			if(finished_count == 2):
				finished_count = 0
				num_moves += 1
				moves_left = num_moves
			else:
				moves_left = num_moves
	return grid

def sumDiagonals(grid):
	size = len(grid)
	total = 0
	for x in range(size):
		if(x == size//2):
			total += grid[x][x]
		else:
			total += grid[x][x] + grid[x][size-1-x]
	return total

size = 1001
total = sumDiagonals(makeSpiral(size))

t = time.time() - t

print("\nThe sum of the diagonals of a %d x %d spiral is %d\nTook %.3f seconds\n" % (size, size, total, t))