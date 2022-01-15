#create variables
import random
import sys


name = input("Hello! What is your name?\n")
print("\n" + name + ", are you ready?!")

count = 0
score = [0 , 0]
keep_playing = True
#define a function to play the game


def game():
    #count = 0
    #score = [0 , 0]
    
    user_action = input("\n\nEnter a choice: rock, paper, or scissors?\n")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    if user_action == computer_action:
        print(f"\n             Both players selected {user_action}. IT'S A TIE!\n")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("\n           ROCK SMASHES SCISSORS! YOU WIN!\n")
            score[0] += 1  
        elif computer_action == "paper":
            print("\n           PAPER COVER ROCK! YOU LOSE.\n")
            score[1] += 1 
        else:
            print("\n           IT'S A TIE!\n")
    elif user_action == "paper":
        if computer_action == "rock":
            print("\n           PAPER COVERS ROCK! YOU WIN!\n")
            score[0] += 1
        elif computer_action == "scissors":
            print("\n           SCISSORS CUTS PAPER! YOU LOSE.\n")
            score[1] += 1
        else:
            print("\n           IT'S A TIE!")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("\n           SCISSORS CUTS PAPER! YOU WIN!\n")
            score[0] += 1
        elif computer_action == "rock":
            print("\n           ROCK SMASHES SCISSORS! YOU LOSE.\n")
            score[1] += 1
        else:
            print("\n           IT'S A TIE!\n")
        
  

    
    
while  count < 5:
    game()
    print("Game #: ", count + 1 ,"\n")
    if count == 6:
        break
    count += 1
    print("Player Score: ", score[0])
    print("Computer Score: ", score[1]) 
    if score[0] > score[1]:
        print("\nYou've won this round!\n\n")
    elif score [0] < score[1]:
        print("\nYou've lost this round!\n\n")
    else: 
        print("\nThis rounds a tie! Great game!\n\n")

