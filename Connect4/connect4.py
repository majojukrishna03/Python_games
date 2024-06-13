players = ["player1","player2"]
discs = ["X","O"]

def initialize_grid():
    grid = []
    for i in range(6):
        a = []
        for j in range(7):
            a.append("-")
        grid.append(a)
    return grid

# grid = initialize_grid()
# print(grid)

def print_grid(grid):
    for i in grid:
        for j in i:
            print(j,end=" ")
        print()

# grid = initialize_grid()
# print_grid(grid)

def get_user_input(grid):
    col = int(input("Enter a col to drop the disc : "))

    while True:
        
        if col < 0 and col > 6:
            print("Invalid column. Please enter a number between 0 and 6.")
        elif all(grid[i][col] != "-" for i in range(len(grid))):
            print("The column is full")
            col = int(input("Enter the another col to drop the disc : "))
            break
        
        else: 
            return col
            
# grid = initialize_grid()
# print_grid(grid)
# get_user_input(grid)
# print_grid(grid)

def drop_disc(grid,col,disc):
    for i in range(len(grid)-1,-1,-1):
        if grid[i][col] == "-":
            grid[i][col] = disc
            return 

# grid = initialize_grid()
# disc = 'X'
# print_grid(grid)
# col = get_user_input(grid)
# drop_disc(grid,col,disc)
# print_grid(grid)


def vertical(grid,disc):
    for col in range(len(grid[0])):
        count = 0
        for row in range(len(grid)):
            if grid[row][col] == disc:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
    return False

def horizontal(grid,disc):
    for row in grid:
        count = 0
        for cell in row:
            if cell == disc:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
    return False


def diagonal(grid,disc):
    for row in range(len(grid) - 3):
        for col in range(len(grid[0]) - 3):
            if all(grid[row+i][col+i] == disc for i in range(4)):
                return True
    return False

def antidiagonal(grid,disc):
    for row in range(len(grid) - 3):
        for col in range(3, len(grid[0])):
            if all(grid[row+i][col-i] == disc for i in range(4)):
                return True
    return False
                


def check_win(grid,disc):
    return (vertical(grid,disc)) or (horizontal(grid,disc)) or (diagonal(grid,disc)) or (antidiagonal(grid,disc))



def check_draw(grid):
    for i in grid:
        for j in i:
            if j == "-":
                return False
    return True


def switch_player(player):
    if player == players[0]:
        player = players[1]
    else: 
        player = players[0]
    return player

def play_game():
    print("Welcome to the game of connect4")
    grid = initialize_grid()
    print_grid(grid)
    player = players[0]

    while True:
        if player == players[0]:
            disc = "X"
        else: 
            disc = "O"
        print(f"{player}'s turn : ")
        col = get_user_input(grid)
        drop_disc(grid,col,disc)
        print_grid(grid)

        if check_win(grid,disc):
            print(f"{player} won the game.")
            break
        
        if check_draw(grid):
            print("Game is draw!!")
            break

        player = switch_player(player)


play_game()






