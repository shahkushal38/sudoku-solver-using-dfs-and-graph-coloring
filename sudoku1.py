import time
import copy

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def problem_state(type):
	type=int(type)
	total = sum(range(1, type+1))

        # Check rows and columns and return false if total is invalid
        for row in range(type):
            if (len(state[row]) != type) or (sum(state[row]) != total):
                return False

            column_total = 0
            for column in range(type):
                column_total += state[column][row]

            if (column_total != total):
                return False

        # Check quadrants and return false if total is invalid
        for column in range(0,type,3):
            for row in range(0,type,height):

                block_total = 0
                for block_row in range(0,height):
                    for block_column in range(0,3):
                        block_total += state[row + block_row][column + block_column]

                if (block_total != total):
                    return False

        return True


def DFS(board):
	if problem_state(9):
		return True
		
def solve_dfs(board):
	print("Solving with DFS - ")
	solution=DFS(board)
