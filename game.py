#game development project (mini project)
#rock,paper,scissors,spoke,lizard....

import random  #random helps to select computer side choice.

   
def play_game():
    #select one choice 
    player_choice = int(input("Enter your choice (1-5): "))
    
    if player_choice not in [1, 2, 3, 4, 5]:
      #exception handling for player entering numbers other than 1,2,3,4,5.
        print("Invalid choice. Please try again.")
        play_game()
    else:
        choices = {1: "Rock", 2: "Paper", 3: "Scissors", 4: "Lizard", 5: "spock"}
        player_choice_name = choices[player_choice]
        #computer choose a options
        computer_choice = random.randint(1, 5)
        computer_choice_name = choices[computer_choice]
        
        print("You chose: ", player_choice_name)
        print("Computer chose: ", computer_choice_name)
        
         
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 1 and computer_choice == 3) or \
             (player_choice == 1 and computer_choice == 4) or \
             (player_choice == 2 and computer_choice == 1) or \
             (player_choice == 2 and computer_choice == 5) or \
             (player_choice == 3 and computer_choice == 2) or \
             (player_choice == 3 and computer_choice == 4) or \
             (player_choice == 4 and computer_choice == 2) or \
             (player_choice == 4 and computer_choice == 5) or \
             (player_choice == 5 and computer_choice == 1) or \
             (player_choice == 5 and computer_choice == 3):
             print("you win!!")

             
            
        else:
            print("Computer wins!")
    
    play_again = input("Do you want to play again? press enter to play again or no to discontinue: ")
    
    if play_again.lower() == "":
        play_game()    #if yes the game restarts
    else :
        print("Thank you for playing!")

#main program starts from here 

print("Welcome to Rock, Paper, Scissors, lizard, spock!")
print("INSTRUCTIONS : You have to choose any one of the following options(1/2/3/4/5) and computer will choose one.")
print("NOTE: scissors cuts paper , paper covers rock , rock crushes lizard , spock smashes scissors , lizard poisons spock, ")
print("scissors decaptitates lizaed , lizard eats paper, paper disproves spock , spock vaporizes rock , rock crushes scissors")

print("1. Rock")
print("2. Paper")
print("3. Scissors")
print("4. Lizard")
print("5. Spock")
play_game()