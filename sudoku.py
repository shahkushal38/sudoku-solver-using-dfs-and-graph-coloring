import pyautogui as pg
import time
import pygame
import matplotlib
pygame.font.init()

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


def print_board(board):
	for i in range(len(board)):
		if(i%3==0 and i!=0):
			print("- - - - - - - - - - - - - - - - - - ")
		for j in range(len(board[0])):
			if(j%3==0 and j!=0):
				print(" | ", end=" ")
			if(j==8):
				print(board[i][j])
			else:
				print(str(board[i][j])+" ",end=" ")

def find_empty(board):
	for i in range(len(board)):
		for j in range(len(board[0])):
			if(board[i][j]==0):
				return (i,j)  #row ,col

	return None;

#to check validity of the answer
def valid(board,num,pos):
	#check row
	for i in range(len(board[0])):
		if(board[pos[0]][i]==num and pos[1]!=i):
			return False

	#check column
	for i in range(len(board)):
		if(board[i][pos[1]]==num and pos[0]!=1):
			return False

	#check box
	box_x=pos[1]//3
	box_y=pos[0]//3

	for i in range(box_y*3, box_y*3 + 3):
   		for j in range(box_x*3, box_x*3 + 3):
		    if( board[i][j] == num and (i,j) != pos):
   	        	return False

	return True

final_stack=[]
def solve(board):
	find=find_empty(board)
	if not find:
		return True
	else:
		row,col=find
		stack=[]
		stack.append(row)   #row and column get append to list
		stack.append(col)
		final_stack.append(stack) # the list gets added to the final stack
		print(final_stack)
	for i in range(1,10,1):
		if(valid(board,i,(row,col))):
			board[row][col]=i

			if(solve(board)):
				return True

			board[row][col]=0
			final_stack.pop()
	return False

class Grid:
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.model = None
        self.selected = None

    def draw(self, win):
        # Draw Grid Lines
        gap = self.width / 9
        for i in range(self.rows+1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(win, (0,0,0), (0, i*gap), (self.width, i*gap), thick)
            pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)

        # Draw Cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.board[i][j].draw(win)

def redraw_window(win, board):
    win.fill((255,255,255))
    # Draw time
    fnt = pygame.font.SysFont("comicsans", 40)
    text = fnt.render("Time: " + format_time(time), 1, (0,0,0))
    win.blit(text, (540 - 160, 560))
    # Draw Strikes
    text = fnt.render("X " * strikes, 1, (255, 0, 0))
    win.blit(text, (20, 560))
    # Draw grid and board
    board.draw(win)




start_time=time.time()
print_board(board)
print("-------------------------------------")
print(final_stack)
solve(board)
print("The solved sudoku solver is: ")
print("--------------------------")
print_board(board)
elapsed_time=time.time()-start_time
print("The Time taken to solve: ",elapsed_time) 

win = pygame.display.set_mode((540,600))
pygame.display.set_caption("Sudoku")
board = Grid(9, 9, 540, 540)
key=None
run=True

pygame.display.update()

pygame.quit()