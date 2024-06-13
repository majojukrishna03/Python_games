import random


def create_deck():
    values = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    deck = values * 4
    random.shuffle(deck)
    return deck


# print(create_deck())

def deal_cards(deck):
    player_hand = [deck.pop(),deck.pop()]
    dealer_hand = [deck.pop(),deck.pop()]
    return player_hand,dealer_hand

def calculate_score(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        # Convert Ace from 11 to 1 if the score is over 21
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score


def play_game():
    print("Welcome to the game of blackjack. ")
    deck = create_deck()
    player_cards,dealer_cards = deal_cards(deck)
    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)
    print(f"your cards : {player_cards}, your score : {player_score}")
    print(f"dealer cards : {dealer_cards[0],'hidden'}")

    while player_score <= 21:
        option = input("Enter 'h' for hit and 's' for stand: ").strip().lower()
        if option == 'h':
            player_cards.append(deck.pop())
            player_score = calculate_score(player_cards)
            print(f"Your cards: {player_cards}, your score: {player_score}")
            if player_score > 21:
                print("Player busts! Dealer wins.")
                return
        elif option == 's':
            print(f"Player stands with score: {player_score}")
            break
        else:
            print("Invalid input. Please enter 'h' to hit or 's' to stand.")
    
    print(f"Dealer's cards: {dealer_cards}, dealer's score: {dealer_score}")
    
    while dealer_score < 17:
        dealer_cards.append(deck.pop())
        dealer_score = calculate_score(dealer_cards)
        print(f"Dealer's cards: {dealer_cards}, dealer's score: {dealer_score}")
    
    if dealer_score > 21:
        print("Dealer busts! Player wins.")
    elif player_score > dealer_score:
        print("Player wins!")
    elif dealer_score > player_score:
        print("Dealer wins!")
    else:
        print("It's a draw!")


play_game()
            

