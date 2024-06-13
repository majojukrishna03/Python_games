import random

def getUserChoice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")

def getComputerChoice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determineWinner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif user_choice == 'rock':
        if computer_choice == 'scissors':
            return 'user'
        else:
            return 'computer'
    elif user_choice == 'paper':
        if computer_choice == 'rock':
            return 'user'
        else:
            return 'computer'
    elif user_choice == 'scissors':
        if computer_choice == 'paper':
            return 'user'
        else:
            return 'computer'

def playRockPaperScissors():

    print("Welcome to the game of Rock-Paper-Scissors!")
    
    while True:
        user_choice = getUserChoice()
        computer_choice = getComputerChoice()
        print(f"Computer chose: {computer_choice}")
        
        winner = determineWinner(user_choice, computer_choice)
        if winner == 'tie':
            print("It's a tie!")
        elif winner == 'user':
            print("You win!")
        else:
            print("Computer wins!")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break


playRockPaperScissors()
