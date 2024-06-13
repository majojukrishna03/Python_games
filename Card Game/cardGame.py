import random

def Deck():
    suits = ['Diamond','Spade','Club','Heart']
    cards = ['2','3','4','5','6','7','8','9','Ace','Jack','Queen','King']
    card_pair = []
    for suit in suits:
        for card in cards:
            card_pair.append([card,suit])
    return card_pair

def Shuffle_deck():
    a = Deck()
    random.shuffle(a)
    player_1_cards = a[:26]
    player_2_cards = a[26:]
    return player_1_cards,player_2_cards

def Score_cal(card):
    score = 0
    score_cards = {'Ace':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'Jack':10,'Queen':10,'King':10}
    if card[0] in score_cards:
        score += score_cards[card[0]]
    return score

def main():
    print("Welcome to the cardGame!!")
    player_1,player_2 = Shuffle_deck()
    # print("Player_1 cards: ",player_1)
    # print("Player_2 cards: ",player_2)

    player_1_score = 0
    player_2_score = 0

    while ((len(player_1) != 0) and (len(player_2) != 0)):
        entry_1 = input("Enter a card with suit for player_1: ")
        card_1 = entry_1.split(" ")
        entry_2 = input("Enter a card with suit for player_2: ")
        card_2 = entry_2.split(" ")

        if card_1 not in player_1 and card_2 in player_2:
            print("card_1 not in player_1 hand")
            print("-------------------------------------------------")
            continue
        elif card_1 in player_1 and card_2 not in player_2:
            print("card_2 not in player_2 hand")
            print("-------------------------------------------------")
            continue
        elif card_1 not in player_1 and card_2 not in player_2:
            print("Cards are not in specific hands")
            print("-------------------------------------------------")
            continue
        else: 
            print("Cards are in Specific hands")
            print("-------------------------------------------------")
            player_1_score += Score_cal(card_1)
            player_1.remove(card_1)

            player_2_score += Score_cal(card_2)
            player_2.remove(card_2)

            print("Respective Scores are: ")
            print("Player_1_score: ", player_1_score)
            print("Player_2_score: ", player_2_score)
            print("-------------------------------------------------")
            
        

        
    if player_1_score > player_2_score:
        print("Congratulations Player_1, You won the game")
    else:
        print("Congratulations Player_2, You won the game")

main()