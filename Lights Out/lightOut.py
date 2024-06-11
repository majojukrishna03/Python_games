import random

def initialize_grid():
    grid = []
    for i in range(5):
        a = []
        for j in range(5):
            b = random.choice([0,1])
            a.append(b)
        grid.append(a)
    return grid

# print(initialize_grid())

def print_grid(grid):
    for i in grid:
        for j in i:
            print(j, end=" ")
        print()

# grid = initialize_grid()
# print_grid(grid)

def get_user_input():
    row = int(input("Enter a row to toggle: "))
    col = int(input("Enter a col to toggle: "))
    while True:
        if (0 <= row <= 4) and (0 <= col <= 4):
            return row,col 
        else: 
            print("Given inputs are not in the grid range")  
            row = int(input("Enter a correct row to toggle: "))
            col = int(input("Enter a correct col to toggle: "))

# get_user_input()

def toggle_light(grid,row,col):
    directions = [(0,0),(0,1),(0,-1),(-1,0),(1,0)]
    for dr,dc in directions:
        r = row + dr
        c = col + dc
        # for edge cases , but not working as the game still no ends
        # if (row == 0 and (0 <= col <= 4)) or (row == 4 and (0 <= col <= 4)) or (col == 0 and (0 <= row <= 4)) or (col == 4 and (0 <= row <= 4)):
        #     if grid[row][col] == 1:
        #         grid[row][col] = 0
        if (0 <= r <= 4) and (0 <= c <= 4):
            if grid[r][c] == 1:
                grid[r][c] = 0
            else: 
                grid[r][c] = 1
        


# grid = initialize_grid()
# print("current grid : ")
# print_grid(grid)
# row,col = get_user_input()
# grid_1 = toggle_light(grid,row,col)
# print("New grid : ")
# print_grid(grid_1)

def check_win(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != 0:
                return False
    return True

def playGame():
    print()
    print("Welcome to the lights off game.")
    print()
    grid = initialize_grid()
    print("Current Grid : ")
    print()
    print_grid(grid)
    while check_win(grid) != True: 
        print()
        row,col = get_user_input()
        toggle_light(grid,row,col)
        print("Current Grid : ")
        print()
        print_grid(grid)

        if check_win(grid) == True:
            return
    print("Congrats, you have toggled all the lights off. ")
    

playGame()
