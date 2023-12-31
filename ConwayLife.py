import tkinter as tk
from tkinter import ttk
import random as rand

# Globals
GOL_BOARD =[]
root = tk.Tk()
boardOutput = tk.Label(root, text="")
boardOutput.pack()

# Prints game board to terminal for debugging purposes
def printTerm(board):
    for row in board:
        for idx in row:
            print(idx, end="")
        print()

def nextGen():
    boardStr = ""
    print("updated")

    temp = []
    for x in range(0, 9):
        nextRow = []
        for y in range(0, 9):
            if rand.randrange(1, 6) == 3: nextRow.append(str(1))
            else: nextRow.append(str(0))
        temp.append(nextRow)

    for row in temp:
        for idx in row:
            boardStr += idx
        boardStr += "\n"
    boardOutput.configure(text=boardStr)
    root.after(1000, nextGen)

# Randomly populates the game board for the initial state
def randPopulate():
    for x in range(0, 9):
        nextRow = []
        for y in range(0, 9):
            if rand.randrange(1, 6) == 3: nextRow.append(str(1))
            else: nextRow.append(str(0))
        GOL_BOARD.append(nextRow)

def main():
    # Window initializations
    root.title("Conway's Game of Life")
    root.geometry("400x400+200+100")

    printTerm(GOL_BOARD)
    randPopulate()
    root.after(1000, nextGen)

    root.mainloop()

if __name__ == "__main__":
    main()
