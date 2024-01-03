import tkinter as tk
from tkinter import ttk
import random as rand

# Globals
dimensions = 25
alive = "*"
dead = " "
root = tk.Tk()
boardOutput = tk.Label(root, text="", font="TkFixedFont")
boardOutput.pack()


# Prints game board to terminal for debugging purposes
def printTerm(board):
    for row in board:
        for idx in row:
            print(idx, end="")
        print()

def findStatus(GoLBoard, x, y):
    wrap = dimensions - 1
    count = 0

    # Find life status of top/bottom row neighbors
    if y < dimensions - 1:
        if x < dimensions - 1:
            for offset in range(-1, 2):
                if GoLBoard[y - 1][x + offset] == alive: count += 1
                if GoLBoard[y + 1][x + offset] == alive: count += 1
            if GoLBoard[y][x - 1] == alive: count += 1
            if GoLBoard[y][x + 1] == alive: count += 1
        else :
            for offset in range(-1, 1):
                if GoLBoard[y - 1][x + offset] == alive: count += 1
                if GoLBoard[y + 1][x + offset] == alive: count += 1
            if GoLBoard[y - 1][x - wrap] == alive: count += 1
            if GoLBoard[y][x - 1] == alive: count += 1
            if GoLBoard[y][x - wrap] == alive: count += 1
            if GoLBoard[y + 1][x - wrap] == alive: count += 1
    else:
        if x < dimensions - 1:
            for offset in range(-1, 2):
                if GoLBoard[y - 1][x + offset] == alive: count += 1
                if GoLBoard[y - wrap][x + offset] == alive: count += 1
            if GoLBoard[y][x - 1] == alive: count += 1
            if GoLBoard[y][x + 1] == alive: count += 1
        else :
            for offset in range(-1, 1):
                if GoLBoard[y - 1][x + offset] == alive: count += 1
                if GoLBoard[y - wrap][x + offset] == alive: count += 1
            if GoLBoard[y - 1][x - wrap] == alive: count += 1
            if GoLBoard[y][x - 1] == alive: count += 1
            if GoLBoard[y][x - wrap] == alive: count += 1
            if GoLBoard[y - wrap][x - wrap] == alive: count += 1

    if count == 3:
        # Survived OR Reproduction
        return 1
    elif count == 2:
        if GoLBoard[y][x] == alive:
            # Survived
            return 1
        else:
           # Dead, not enough for Reproduction
            return 0
    else:
        # Dead
        return 0


def nextGen(board):
    boardStr = ""

    nextBoard = []
    for y in range(0, dimensions):
        nextRow = []
        for x in range(0, dimensions * 3):
            if findStatus(board, x, y) == 1: nextRow.append(alive)
            else: nextRow.append(dead)
        nextBoard.append(nextRow)

    for row in nextBoard:
        for idx in row:
            boardStr += idx
        boardStr += "\n"
    boardStr.format()
    boardOutput.configure(text=boardStr)
    # Set board global to the next generation
    root.after(1000, nextGen, nextBoard)

# Randomly populates the game board for the initial state
def randPopulate():
    board = []
    for y in range(0, dimensions):
        nextRow = []
        for x in range(0, dimensions * 3):
            if rand.randrange(1, 11) == 1: nextRow.append(alive)
            else: nextRow.append(dead)
        board.append(nextRow)
    return board


def main():
    # Window initializations
    root.title("Conway's Game of Life")
    root.geometry("400x400+200+100")

    # GoLBoard indexing goes [y-axis][x-axis]
    GoLBoard = []

    GoLBoard = randPopulate()
    root.after(1000, nextGen, GoLBoard)

    root.mainloop()

if __name__ == "__main__":
    main()
