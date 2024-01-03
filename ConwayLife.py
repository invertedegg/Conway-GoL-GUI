import tkinter as tk
from tkinter import ttk
import random as rand

# Globals
# GOL_BOARD indexing goes [y-axis][x-axis]
GOL_BOARD =[]
dimensions = 5
root = tk.Tk()
boardOutput = tk.Label(root, text="")
boardOutput.pack()

# Prints game board to terminal for debugging purposes
def printTerm(board):
    for row in board:
        for idx in row:
            print(idx, end="")
        print()

def findStatus(x, y):
    print("caught:", str(y), str(x))
    wrap = dimensions - 1
    count = 0

    # Find life status of top/bottom row neighbors
    if y < dimensions - 1:
        if x < dimensions - 1:
            for offset in range(-1, 2):
                if GOL_BOARD[y - 1][x + offset] == "1": count += 1
                if GOL_BOARD[y + 1][x + offset] == "1": count += 1
            if GOL_BOARD[y][x - 1] == "1": count += 1
            if GOL_BOARD[y][x + 1] == "1": count += 1
        else :
            for offset in range(-1, 1):
                if GOL_BOARD[y - 1][x + offset] == "1": count += 1
                if GOL_BOARD[y + 1][x + offset] == "1": count += 1
            if GOL_BOARD[y - 1][x - wrap] == "1": count += 1
            if GOL_BOARD[y][x - 1] == "1": count += 1
            if GOL_BOARD[y][x - wrap] == "1": count += 1
            if GOL_BOARD[y + 1][x - wrap] == "1": count += 1
    else:
        if x < dimensions - 1:
            for offset in range(-1, 2):
                if GOL_BOARD[y - 1][x + offset] == "1": count += 1
                if GOL_BOARD[y - wrap][x + offset] == "1": count += 1
            if GOL_BOARD[y][x - 1] == "1": count += 1
            if GOL_BOARD[y][x + 1] == "1": count += 1
        else :
            for offset in range(-1, 1):
                if GOL_BOARD[y - 1][x + offset] == "1": count += 1
                if GOL_BOARD[y - wrap][x + offset] == "1": count += 1
            if GOL_BOARD[y - 1][x - wrap] == "1": count += 1
            if GOL_BOARD[y][x - 1] == "1": count += 1
            if GOL_BOARD[y][x - wrap] == "1": count += 1
            if GOL_BOARD[y - wrap][x - wrap] == "1": count += 1

    if count == 3:
        print("Survived OR Reproduction")
    elif count == 2:
        if GOL_BOARD[y][x] == "1":
            print("Survived")
        else:
            print("Dead, not enough for Reproduction")
    else:
        print("Dead")
    print()


def nextGen():
    boardStr = ""
    print("updated")

    temp = []
    for y in range(0, dimensions):
        nextRow = []
        for x in range(0, dimensions):
            print("Find status on point:", str(y), str(x))
            findStatus(x, y)
            # if rand.randrange(1, 6) == 3: nextRow.append(str(1))
            # else: nextRow.append(str(0))
        # temp.append(nextRow)

    for row in temp:
        for idx in row:
            boardStr += idx
        boardStr += "\n"
    boardOutput.configure(text=boardStr)
    root.after(1000, nextGen)

# Randomly populates the game board for the initial state
def randPopulate():
    for y in range(0, dimensions):
        nextRow = []
        for x in range(0, dimensions):
            if rand.randrange(1, 6) == 3: nextRow.append(str(1))
            else: nextRow.append(str(0))
        GOL_BOARD.append(nextRow)


def main():
    # Window initializations
    # root.title("Conway's Game of Life")
    # root.geometry("400x400+200+100")

    randPopulate()
    printTerm(GOL_BOARD)
    nextGen()
    # root.after(1000, nextGen)

    # root.mainloop()

if __name__ == "__main__":
    main()
