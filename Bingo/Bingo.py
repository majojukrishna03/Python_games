import random

Board = []
def generateBoard(n):
    for i in range(n):
        row = random.sample(range(1,101),n)
        Board.append(row)
    return Board

def displayBoard(board):
    for i in board:
        for j in i:
            print(j, end= " ")
        print()
    return None

def markNumber(board,number):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == number:
                board[i][j] = 'X'
    return None

# n = int(input("Enter a number to generate n*n board: "))
# board = generateBoard(n)
# displayBoard(board)

# number = int(input("Enter a number from board: "))
# markNumber(board,number)
# displayBoard(board)

def getUserNumber():
    number = int(input("Enter a number between 1 and 100: "))
    if 0 < number <= 100:
        return number
    elif number < 0 or number > 100:
        print("Invalid number. Please enter a valid number between 1 and 100")
    else:
        print("Invalid input!!.Enter a number between 1 and 100")
    

def vertical(board):
    for j in range(len(board)):
        all_x = True
        for i in range(len(board)):
            if board[i][j] != 'X' :
                all_x = False
                break
        if all_x:
            return True
    return False 
    


def horizontal(board):
    for i in board:
        all_x = True
        for j in i:
            if j != 'X' :
                all_x = False
                break
        if all_x:
            return True
    return False


def diagonal(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i==j:
                if board[i][j] != 'X' :
                    return False
    return True 

def antidiagonal(board):
    for i in range(len(board)):
        if board[i][len(board)-1-i] != 'X':
            return False
    return True 

def checkWin(board):

    if vertical(board) == True or horizontal(board) == True or diagonal(board) == True or antidiagonal(board) == True:
        return True
    else:
        return False





def playBingoGame():
    print()
    print("Welcome to the Bingo Game.")
    n = int(input("Enter a number to generate n*n board: "))
    board = generateBoard(n)
    # print(board)
    displayBoard(board)
    while True: 
        number = getUserNumber()
        markNumber(board,number)
        displayBoard(board)

        if checkWin(board) == True: 
            print("congrats, you won")
            break
        else: 
            continue


playBingoGame()