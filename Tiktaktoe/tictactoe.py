players = ['player_1','player_2']

def initialize_grid(n):
    grid = []
    for i in range(n):
        a = []
        for j in range(n):
            b = "-"
            a.append(b)
        grid.append(a)

    return grid

# n = int(input("Enter a size of a grid : "))
# print(initialize_grid(n))

def display_grid(grid):
    for i in grid:
        for j in i:
            print(j,end= ' ')
        print()
    

# n = int(input("Enter a size of a grid : "))
# grid = (initialize_grid(n))
# display_grid(grid)

def get_user_input(n):
    row = int(input("Enter the row to place the mark : "))
    col = int(input("Enter the col to place the mark : "))
    while True: 
        if (0 <= row <= n-1) and (0 <= col <= n-1):
            return row,col
        else: 
            print(f"Enter the row and col in the range of 0-{n-1}")
            row = int(input("Enter the correct row to place the mark : "))
            col = int(input("Enter the correct col to place the mark : "))

# n = int(input("Enter a size of a grid : "))
# grid = (initialize_grid(n))
# display_grid(grid)
# row,col = get_user_input(n)

def place_mark(grid,row,col,mark):
    if grid[row][col] == "-":
        grid[row][col] = mark
    else: 
        print("This position is already marked.")
    return grid

# n = int(input("Enter a size of a grid : "))
# grid = (initialize_grid(n))
# display_grid(grid)
# row,col = get_user_input(n)
# grid_1 = place_mark(grid,row,col,mark="X")
# display_grid(grid_1)

def vertical(grid,mark):
    for col in range(len(grid)):
        if all(grid[row][col] == mark for row in range(len(grid))):
            return True
    return False

def horizontal(grid,mark):
    for row in grid:
        if all(cell == mark for cell in row):
            return True
    return False


def diagonal(grid,mark):
    if all(grid[i][i] == mark for i in range(len(grid))):
        return True
    return False

def antidiagonal(grid,mark):
    n = len(grid)
    if all(grid[i][n-1-i] == mark for i in range(n)):
        return True
    return False
                


def checkWin(grid,mark):
    return (vertical(grid,mark)) or (horizontal(grid,mark)) or (diagonal(grid,mark)) or (antidiagonal(grid,mark))
    
    
def checkDraw(grid):
    for i in grid:
        if "-" in i:
            return False
    return True
    

def switchPlayer(player):
    if player == players[0]:
        player = players[1]
    else:
        player = players[0]
    return player


def playGame():
    print("Welcome to the game of tic tac toe.")
    n = int(input("Enter the size of grid : "))
    grid = initialize_grid(n)
    display_grid(grid)
    player = players[0]
    while True:
        if player == players[0]:
            mark = "X"
        else:
            mark = "O"
        print(f"This is {player} chance. ")
        row,col = get_user_input(n)
        grid = place_mark(grid,row,col,mark)
        display_grid(grid)
        
        if checkWin(grid,mark):
            print(f"Congrats, {player}. You won the game.")
            return 
        elif checkDraw(grid):
            print("The game is draw.")
            return
            
        player = switchPlayer(player)
    
    
    
playGame()

    