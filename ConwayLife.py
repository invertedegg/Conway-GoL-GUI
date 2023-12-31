import random as rand

# Global to be made into a matrix representing the game board
GOL_BOARD =[]

# Prints game board to terminal for debugging purposes
def printTerm(board):
    for row in board:
        for idx in row:
            print(idx, end="")
        print()

# Randomly populates the game board for the initial state
def randPopulate():
    for x in range(0, 9):
        nextRow = []
        for y in range(0, 9):
            if rand.randrange(1, 6) == 3: nextRow.append(1)
            else: nextRow.append(0)
        GOL_BOARD.append(nextRow)


def main():
    randPopulate()
    printTerm(GOL_BOARD)

if __name__ == "__main__":
    main()
