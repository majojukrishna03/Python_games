import random

def initialize_game():
    n = random.randint(1,101)
    return n

def get_player_guess():
    guess = int(input("Enter a number to guess in the range 1-100 :"))
    while True:    
        if (1 <= guess < 101):
            return guess
        else: 
            print("Enter the number in the given range")
            guess = int(input("Enter a number to guess in the range 1-100 :"))
        
def provide_feedback(n,guess):
    if guess > n:
        return "Too high"
    elif guess < n:
        return "too low"
    else: 
        return "Correct guess"
    
def checkWin(a):
    if a == "Correct guess":
        return True
    else: 
        return False

def play_game():
    n = initialize_game()
    while True: 
        guess = get_player_guess()
        feedback = provide_feedback(n,guess)
        print(feedback)

        if checkWin(feedback):
            print("Congrats you win")
            break
        
play_game()


    