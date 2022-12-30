import os # For clear() function
import random
import art
import game_data

def game():
    score = 0
    A = random.choice(game_data.data)
    
    game = True
    while game is True:
        print(art.logo)
        # Print score if not the first round.
        if score > 0:
            print(f"You're right! Current score: {score}.")
        B = random.choice(game_data.data)
        # Check to make sure A isn't the same as B and if it is, randomise again.
        while A == B:
            B = random.choice(game_data.data)
        print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
        print(art.vs)
        print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
        
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        if A['follower_count'] > B['follower_count'] and answer == "a":
            score += 1
            A = B
            os.system('cls||clear')
        elif B['follower_count'] > A['follower_count'] and answer == "b":
            score += 1
            A = B
            os.system('cls||clear')
        else:
            os.system('cls||clear')
            print(art.logo)
            print(f"Sorry that's wrong. Final score: {score}.")
            game = False

game()