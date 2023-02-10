###############     Blackjack Project     #####################

import os # For clear screen functionality
import random
from art import logo

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

###############################################################

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():

    player_cards = []
    player_score = 0
    dealer_cards = []
    dealer_score = 0

    new_game = True

    while new_game == True:

        print(logo)
        
        player_cards = random.sample(cards, 2)
        player_score = sum(player_cards)
        dealer_cards = random.sample(cards, 1)
        dealer_score = sum(dealer_cards)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_score}")

        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == "y":
            player_cards.append(random.choice(cards))
            player_score = sum(player_cards)

            # Scoring
            print(f"Your final hand: {player_cards}, final score: {player_score}")
            if player_score > 21:
                print("You went bust. You loose.")
            else:
                dealer_cards.append(random.choice(cards))
                dealer_score = sum(dealer_cards)
                if len(dealer_cards) == 2 and dealer_score < 17:
                    dealer_cards.append(random.choice(cards))
                    dealer_score = sum(dealer_cards)
                print(f"Dealer's final hand: {dealer_cards}, dealer's final score: {dealer_score}")
                if dealer_score > 21:
                    print("Dealer went bust. You win!")
                elif dealer_score == player_score:
                    print("Draw.")
                elif dealer_score > player_score:
                    print("Dealer wins.")
                else:
                    print("You win!")
        
        else:
            # Scoring
            print(f"Your final hand: {player_cards}, final score: {player_score}")
            if player_score > 21:
                print("You went bust. You loose.")
            else:
                dealer_cards.append(random.choice(cards))
                dealer_score = sum(dealer_cards)
                if len(dealer_cards) == 2 and dealer_score < 17:
                    dealer_cards.append(random.choice(cards))
                    dealer_score = sum(dealer_cards)
                print(f"Dealer's final hand: {dealer_cards}, dealer's final score: {dealer_score}")
                if dealer_score > 21:
                    print("Dealer went bust. You win!")
                elif dealer_score == player_score:
                    print("Draw.")
                elif dealer_score > player_score:
                    print("Dealer wins.")
                else:
                    print("You win!")
                
        play_game = input("Would you like to play a game of blackjack? Type 'y' or 'n': ")
        if play_game == 'n':
            new_game = False
        os.system('cls||clear')

blackjack()