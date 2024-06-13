import random

ladders = {3:15, 9:45, 19:35, 29:78, 54:99}
snakes = {98:56, 84:67, 72:43, 45:21, 23:2}
players = {}

def generateBoard():
    
    board = []
    for i in range(1,101):
        board.append(i)

    return board,ladders,snakes

# print(generateBoard())

def print_board():
    print("Snakes and Ladders positions :")
    print(f"Ladders : {ladders}")
    print(f"Snakes : {snakes}")

def register_players():
    num_players = int(input("Enter the number of players : "))
    for i in range(1,num_players + 1):
        name = input(f"Enter the name of player {i} : ")
        players[name] = 1 
    return players


def roll_die():
    return random.randint(1,6)

def move_player(player,position,ladders,snakes):
    print(f" {player}'s turn. Current position: {position}")
    roll = roll_die()
    print(f" {player} rolled a {roll}")
    new_position = position + roll
    
    if new_position > 100:
        new_position = position
    
    if new_position in ladders:
        print(f"Encountered a ladder! climbing it. ")
        new_position = ladders[new_position]

    elif new_position in snakes:
        print(f"Encountered a snake!! sliding down.")
        new_position = snakes[new_position]
    
    print(f" {player} moves to position {new_position}")
    return new_position

def check_win(postiion):
    return postiion == 100

def display_positions(players):
    print("Current Positions: ")
    for player,position in players.items():
        print(f"{player} : {position}")

def play_game():
    print("Welcome to the snake and ladder game.")
    board,ladders,snakes = generateBoard()
    print_board()
    players = register_players()
    win = False
    
    while not win:
        for player in players.keys():
            new_position = move_player(player, players[player], ladders, snakes)
            players[player] = new_position
            display_positions(players)

            if check_win(new_position):
                print(f"{player} wins!")
                win = True
                break

play_game()



