#create variables
import random


name = input("Hello! What is your name?\n")
print("\n" + name + ", are you ready?!")

count = 0
#define a function to play the game

def game():
    count = 0
    score = [0 , 0]
    user_action = input("Enter a choice:\nrock, paper, or scissors?\n")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    if user_action == computer_action:
        print(f"\n          Both players selected {user_action}. It's a tie!\n")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("\n           Rock smashes scissors! You win!\n")
            score[0] += 1  
        elif computer_action == "paper":
            print("\n           Paper covers rock! You lose.\n")
            score[1] += 1 
        else:
            print("\n           It's a tie!\n")
    elif user_action == "paper":
        if computer_action == "rock":
            print("\n           Paper covers rock! You win!\n")
            score[0] += 1
        elif computer_action == "scissors":
            print("\n           Scissors cuts paper! You lose.\n")
            score[1] += 1
        else:
            print("\nIts a tie!")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("\n           Scissors cuts paper! You win!\n")
            score[0] += 1
        elif computer_action == "rock":
            print("\n           Rock smashes scissors! You lose.\n")
            score[1] += 1
        else:
            print("\nIt's a tie!\n")
    count += 1    
    print("Player Score: ", score[0])
    print("Computer Score: ", score[1])

while count < 5:
    game()
    print("Game #: ", count + 1 ,"\n")
    if count == 6:
        break
    count += 1   
           


    
    
    
    
    
    
    
    
    #call the function numbnuts 
   

        # def gameLoop(count):
            
        #     if count < 5:
        #         game()
        #         count += 1
        #         print(count)
        #     elif count == 5:
        #         print("Player Score: ", game.score[0])
        #         print("Computer Score: ", game.score[1])
        #         print("Game #: ", count)
        #     else:
        #         pass
            


        


    #define a function that loops the game 5 times
    # def game_five():
    #     if count < 5:
    #         game()
    #     else:
    #         print(counter(player1))
    #         print(counter())










        # loop_five(count_user)

        # #    loop_five_comp(count_comp)
        # print("Player:", score[0])

        # print("Computer:", score[1])


        # #define function that prints the score and who won
        # score = 0
        # def final_score():
        #     score = 0
        #     if user_action.score < 3:
        #         print("You lose!")
        #     else:
        #         print("You Win!")


        # # #define a function to keep count (1 funct for user 1 funct for comp)
        # # def counter(player1):
        # #     count = 0
        # #     if player1 == "rock":
        # #         count += 1
        # #     elif player1 == "scissors":
        # #         count += 0
        # #     else:
        # #         count +=0




# #define a function to only play game 5 times before printing the winner/count
# def game_five(game()):
#     if count < 5:
#         game()
#     else:
#         print(counter(player1))
#         print(counter())