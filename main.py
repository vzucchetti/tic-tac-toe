# --------------------------------------------------------------------------------------------------------------------------------------------
# HASH GAME PROJECT
# --------------------------------------------------------------------------------------------------------------------------------------------
# Developing a hash game where the user must play against the computer.
# The computer will make random moves.
# The name of the winners must be saved in a .txt file.
# --------------------------------------------------------------------------------------------------------------------------------------------

import random


# --------------------------------------------------------------------------------------------------------------------------------------------
# Function generating the game's initial board; creates a nested list with 3 rows and 3 columns filled
# with "#" to signal that they have not been occupied in the game
# --------------------------------------------------------------------------------------------------------------------------------------------
def generateBoard():
    board = []
    for col in range(3):
        row = []
        for lin in range(3):
            row.append("#")
        board.append(row)
    return board


# --------------------------------------------------------------------------------------------------------------------------------------------
# Function to print the board for user viewing
# --------------------------------------------------------------------------------------------------------------------------------------------
def writeBoard(board):
    print("\n-------------Hash Game-------------")
    indexes = [0, 1, 2]
    print("\t\t0\t1\t2")
    # Print the row and column values
    for i in indexes:
        print("\t", i, "\t", end="")
        for j in indexes:
            print(board[i][j], "\t", end="")
        print()


# --------------------------------------------------------------------------------------------------------------------------------------------
# Function for the computer to make your move randomly
# --------------------------------------------------------------------------------------------------------------------------------------------
def moveComputer(board):
    row = random.randint(0, 2)
    column = random.randint(0, 2)
    # Validation with loop to check free positions on the board
    while board[row][column] != "#":
        row = random.randint(0, 2)
        column = random.randint(0, 2)
    board[row][column] = "O"


# --------------------------------------------------------------------------------------------------------------------------------------------
# Function to check the validity of the move within the board's row and column indexes
# --------------------------------------------------------------------------------------------------------------------------------------------
def valid(value):
    if value >= 0 and value <= 2:
        return True
    return False


# --------------------------------------------------------------------------------------------------------------------------------------------
# Function to user make your move
# --------------------------------------------------------------------------------------------------------------------------------------------
def moveUser(board):
    print()
    # Insertion of the row and column value that the user wants to make their move
    row = int(input("\tInform the row:"))
    column = int(input("\tInform the column:"))
    # Validation with loop to check free positions in row and column on the board; remember to always validate the indexes first and then validate the access,
    # if not, returns a execution error
    while not (valid(row)) or not (valid(column)) or not (board[row][column] == "#"):
        print("\tIndexes outside the valid interval or occupied cell")
        row = int(input("\tInform the row:"))
        column = int(input("\tInform the column:"))
    board[row][column] = "X"


# --------------------------------------------------------------------------------------------------------------------------------------------
# Function to check the rows on the board
# --------------------------------------------------------------------------------------------------------------------------------------------
def verifyWinnerInRow(board, character):
    for row in board:
        count = 0
        for item in row:
            if item == character:
                count = count + 1
            else:
                count = 0
                break
        if count == 3:
            return True
    return False


# --------------------------------------------------------------------------------------------------------------------------------------------
# Function to check the columns on the board
# --------------------------------------------------------------------------------------------------------------------------------------------
def verifyWinnerInColumn(board, character):
    col = 0
    while col <= 2:
        lin = 0
        count = 0
        while lin <= 2:
            if board[lin][col] == character:
                count = count + 1
            else:
                count = 0
                break
            lin = lin + 1
        if count == 3:
            return True
        col = col + 1
    return False


# --------------------------------------------------------------------------------------------------------------------------------------------
# Function to check the diagonals on the board
# --------------------------------------------------------------------------------------------------------------------------------------------
def verifyWinnerInDiagonal(board, character):
    count = 0
    # Checking the main diagonal
    for i in range(3):
        if board[i][i] == character:
            count = count + 1
        else:
            break
    if count == 3:
        return True
    count = 0
    # Checking the secondary diagonal
    for i in range(3):
        if board[i][2 - i] == character:
            count = count + 1
        else:
            break
    if count == 3:
        return True
    return False


# --------------------------------------------------------------------------------------------------------------------------------------------
# Function to check the game winner#--------------------------------------------------------------------------------------------------------------------------------------------
def verifyWinner(board, character):
    # Checking rows on the board
    result = verifyWinnerInRow(board, character)
    if result == True:
        return True
    # Checking columns on the board
    result = verifyWinnerInColumn(board, character)
    if result == True:
        return True
    # Checking diagonals on the board
    result = verifyWinnerInDiagonal(board, character)
    if result == True:
        return True
    return False


# --------------------------------------------------------------------------------------------------------------------------------------------
# Function to run the game
# --------------------------------------------------------------------------------------------------------------------------------------------
def hash():
    tab = generateBoard()
    writeBoard(tab)
    moveUser(tab)

    count = 1
    winner = 0
    # Loop for iteration of moves totaling 8 moves
    while count <= 4:
        moveComputer(tab)
        # Checking whether the play resulted in winning the match
        # Cheking computer move
        r = verifyWinner(tab, "O")
        if r == True:
            winner = 2
            break
        writeBoard(tab)
        moveUser(tab)
        # Checking user move
        r = verifyWinner(tab, "X")
        if r == True:
            winner = 1
            break
        count = count + 1

    # When loop of moves is finished, print the board and the result of the game
    writeBoard(tab)
    print()
    if winner == 0:
        print("\tIt's a draw!")
    elif winner == 2:
        print("\tThe computer won!")
    else:
        print("\tThe user won!")
    return winner


# --------------------------------------------------------------------------------------------------------------------------------------------
# Function to record game winners
# --------------------------------------------------------------------------------------------------------------------------------------------
def recordWinner(nameWinner, file):
    arq = open(file, "a")
    arq.write(nameWinner + "\n")
    arq.close()


# --------------------------------------------------------------------------------------------------------------------------------------------
# Function to read the winners file and present in the program
# --------------------------------------------------------------------------------------------------------------------------------------------
def readFileWinners(file):
    #'try' to when the program try to make the read of a file that doesn't exist
    try:
        arq = open(file)
    except FileNotFoundError:
        return []
    winners = []
    for row in arq:
        winners.append(row[:-1])
    return winners


# --------------------------------------------------------------------------------------------------------------------------------------------
# Function to the program present the file with the previous game winners
# --------------------------------------------------------------------------------------------------------------------------------------------
def writeList(list):
    print("\nWinners:")
    if list == []:
        print("There are no registered winners so far.")
    for item in list:
        print(item)


# --------------------------------------------------------------------------------------------------------------------------------------------
# Game initial menu; MAIN PROGRAM
# --------------------------------------------------------------------------------------------------------------------------------------------
def main():
    while True:
        print("\n\n----MENU---- ")
        print()
        print("1 - Play")
        print("2 - See previous winners")
        print("0 - Leave game")
        print("\nEnter the option: ")
        op = int(input())
        # option 0 ends the program
        if op == 0:
            print("End of program")
            break
        else:
            # option 1 starts a new game
            if op == 1:
                winner = hash()
                # return 0 in case of draw and record this
                if winner == 0:
                    recordWinner("draw", "results.txt")
                else:
                    # return 1 in case of user wins and asks to enter its name to record in the winner's file
                    if winner == 1:
                        name = input("\tInform your name:")
                        recordWinner(name, "results.txt")
                    # return 2 in case of computer wins and record this
                    else:
                        recordWinner("computer", "results.txt")
            else:
                # option 2 opens the file with the previous game winners
                if op == 2:
                    data = readFileWinners("results.txt")
                    writeList(data)
                else:
                    print("Invalid option")


# --------------------------------------------------------------------------------------------------------------------------------------------
# Running the main function
# --------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
