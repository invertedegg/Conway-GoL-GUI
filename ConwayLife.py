from sys import argv
import tkinter as tk
from tkinter import ttk
import random as rand

# Globals
yDimension = 50
xDimension = yDimension * 3
speed = 250
alive = "*"
dead = " "

# Tkinter Globals
root = tk.Tk()
boardOutput = tk.Label(root, text="", font="TkFixedFont", anchor="n")
boardOutput.pack()

# Prints game board to terminal for debugging purposes
def printTerm(board):
    for row in board:
        for idx in row:
            print(idx, end="")
        print()

# Determines whether the cell at position (x, y) should live or
# die given the rules of Conway's Game of Life
def findStatus(board, x, y):
    wrapy = yDimension - 1
    wrapx = xDimension - 1
    count = 0

    # Find life status of top/bottom row neighbors
    if y < wrapy:
        if x < wrapx:
            for offset in range(-1, 2):
                if board[y - 1][x + offset] == alive: count += 1
                if board[y + 1][x + offset] == alive: count += 1
            if board[y][x - 1] == alive: count += 1
            if board[y][x + 1] == alive: count += 1
        else :
            for offset in range(-1, 1):
                if board[y - 1][x + offset] == alive: count += 1
                if board[y + 1][x + offset] == alive: count += 1
            if board[y - 1][x - wrapx] == alive: count += 1
            if board[y][x - 1] == alive: count += 1
            if board[y][x - wrapx] == alive: count += 1
            if board[y + 1][x - wrapx] == alive: count += 1
    else:
        if x < wrapx:
            for offset in range(-1, 2):
                if board[y - 1][x + offset] == alive: count += 1
                if board[y - wrapy][x + offset] == alive: count += 1
            if board[y][x - 1] == alive: count += 1
            if board[y][x + 1] == alive: count += 1
        else :
            for offset in range(-1, 1):
                if board[y - 1][x + offset] == alive: count += 1
                if board[y - wrapy][x + offset] == alive: count += 1
            if board[y - 1][x - wrapx] == alive: count += 1
            if board[y][x - 1] == alive: count += 1
            if board[y][x - wrapx] == alive: count += 1
            if board[y - wrapy][x - wrapx] == alive: count += 1

    # Set status given amount of living neighbors
    if count == 3:
        # Survived OR Reproduction
        return 1
    elif count == 2:
        if board[y][x] == alive:
            # Survived
            return 1
        else:
           # Dead, not enough for Reproduction
            return 0
    else:
        # Dead
        return 0

# Determines what the next generation of the game board will be
def nextGen(board):
    boardStr = ""

    nextBoard = []
    for y in range(0, yDimension):
        nextRow = []
        for x in range(0, xDimension):
            if findStatus(board, x, y) == 1: nextRow.append(alive)
            else: nextRow.append(dead)
        nextBoard.append(nextRow)

    for row in nextBoard:
        for idx in row:
            boardStr += idx
        boardStr += "\n"
    boardOutput.configure(text=boardStr)
    # Set board global to the next generation
    root.after(speed, nextGen, nextBoard)

# Randomly populates the game board for the initial state
def randPopulate(uSeed):
    board = []

    # Check for user-enetered random seed
    if uSeed != "null":
        print(uSeed)
        rand.seed(int(uSeed))

    for y in range(0, yDimension):
        nextRow = []
        for x in range(0, yDimension * 3):
            if rand.randrange(1, 11) == 1: nextRow.append(alive)
            else: nextRow.append(dead)
        board.append(nextRow)
    return board

def main():
    # Window initializations
    root.title("Conway's Game of Life")
    root.geometry("1250x850+100+0")

    # GoLBoard indexing goes [y-axis][x-axis]
    GoLBoard = []

    if (argv[1] == "-s"):
        GoLBoard = randPopulate(argv[2])
    else:
        GoLBoard = randPopulate("null")
    root.after(speed, nextGen, GoLBoard)

    root.mainloop()

if __name__ == "__main__":
    main()
