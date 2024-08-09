
# !Welcome to Dungeons and Dragons Adventure Story Game.

# *You are a brave adventurer seeking fortune and glory in the land of Eldoria.
# *Your quest begins in the small village of Willowdale, where rumors of a legendary treasure have drawn you and many other adventurers.

# todo: Your goal is to find the treasure and return to the village, but be warned the journey will be fraught with danger, and you will need all your wits and courage to succeed.

#? So Lets begin the adventure :
print("Welcome to Dungeons and Dragons Adventure Story.")

print("You are standing in the middle of a crossroad, which shows the directions to the left and right.")

direction = input("Which direction would you like to choose: left or right? ").lower()
if direction == "left":
    print("You walk down to a forest path and encounter a dragon named Vhagar and another adventurer.")
    print("Are you going to fight the adventurer to claim the dragon, or will you run away?")
    action = input("Type 'claim' or 'run' and hit the Enter: ").lower()
    if action == "claim":
        print("You have to encounter the adventurer and defeat him by playing rock, paper, scissors.")
        print("Are you ready for the game or run away ?")
        action = input("Type 'game' or 'run' and hit the Enter: ").lower()

        if action == "game":
            #todo:  write the code here with rock paper scissors
        
            import random
            #we need 2 variable one for the user and adventurer
            user_wins = 0
            adventurer_wins = 0
            
            # save the list in variable called options
            options = ["rock", "paper", "scissors"]
            while True:
                user_input = input("Type rock/paper/scissors or q to quit: ").lower()
                if user_input == "q":
                    print("GAME OVER")
                    break
                if user_input not in options: #if the user input not in here ie you didnt type valid answer
                    print("Invalid input. Please type rock, paper or scissors.")
                    continue #this will take you back to the question again and it will repeat until you give valid input
                #todo: Generate a random number that represents rock paper scissors for the adventurer.
                random_number = random.randint(0,2)
                # rock is 0, paper is 1 and scissors is 2
                adventurer_pick = options[random_number]
                print(f"Adventurer picked {adventurer_pick}.")
            # to decide who won we need to compare users pick to the computer pick
                if user_input == "rock" and adventurer_pick == "scissors": # 'and' check if the condition on the left side and right side is true.
            #if statement only works if both condition are true.
                    print("You win this round!")
                    user_wins += 1 # this will give one more win
                

                elif user_input == "paper" and adventurer_pick == "rock": 
                    print("You win this round!")
                    user_wins += 1 


                elif user_input == "sciccors" and adventurer_pick == "paper":
                    print("You win this round!")
                    user_wins += 1 
                
                elif user_input == adventurer_pick:
                    print(f"Both player selected {user_input}. its a tie!")
                
                else: 
                    print("You lost ")
                    adventurer_wins += 1

            print(f"You won {user_wins} times.")
            print(f"The adventurer won , {adventurer_wins} times.")
            if user_wins > adventurer_wins:
                print("You won the game you can claim the dragon and treasure map and travel to the island to find treasure!")
            else:
                print("You lost the game, The adventurer claim the dargon and flies aways")
                print("GAME OVER")
        #todo: End of the ROCK PAPER SCISSORS

        elif action == "run":
            print("You run away from the adventurer and dragon and now you are lost in the forest.")
            print("GAME OVER")
        else:
            print("Invalid choice. The adventurer claims the dragon Vhagar and flies away")
            
elif direction == "right":
    print("You walk along a mountain trail and find a mysterious cave.")
    print("Do you want to enter the cave or go back to the village?")   
    action = input("Type 'enter' or 'back' and hit the Enter: ").lower()
    if action == "enter":
        print("You enter the cave and discover a caveman holding the treasure map. ")
        print("In order to get the treasure map you have to defeat the caveman by playing rock, paper and scissors")
        print("Are you ready for the game or run away ?")
        action = input("Type 'game' or 'run' and hit the Enter: ").lower()
        if action == "game":
# Todo: write the code here with rock paper scissors
            import random
            #we need 2 variable one for the user and caveman wins
            user_wins = 0
            caveman_wins = 0
            
            # save the list in variable called options
            options = ["rock", "paper", "scissors"]
            while True:
                user_input = input("Type rock/paper/scissors or q to quit: ").lower()
                if user_input == "q":
                    print("GAME OVER")
                    break
                if user_input not in options: #if the user input not in here ie you didnt type valid answer
                    print("Invalid input. Please type rock, paper or scissors.")
                    continue #this will take you back to the question again and it will repeat until you give valid input
                #todo: Generate a random number that represents rock paper scissors for the Caveman.
                random_number = random.randint(0,2)
                # rock is 0, paper is 1 and scissors is 2
                caveman_pick = options[random_number]
                print(f"Caveman picked {caveman_pick}.")
            # to decide who won we need to compare users pick to the computer pick
                if user_input == "rock" and caveman_pick == "scissors": # 'and' check if the condition on the left side and right side is true.
            #if statement only works if both condition are true.
                    print("You win this round!")
                    user_wins += 1 # this will give one more win
                

                elif user_input == "paper" and caveman_pick == "rock": 
                    print("You win this round!")
                    user_wins += 1 


                elif user_input == "sciccors" and caveman_pick == "paper":
                    print("You win this round!")
                    user_wins += 1 
                
                elif user_input == caveman_pick:
                    print(f"Both player selected {user_input}. its a tie!")
                
                else: 
                    print("You lost ")
                    caveman_wins += 1

            print(f"You won {user_wins} times.")
            print(f"The Caveman won , {caveman_wins} times.")
            if user_wins > caveman_wins:
                print("You won the game, you defeat the Caveman and took the treasure map and travel to the island to find the treasure!")
            else:
                print("You lost the game, The Caveman push you from the top of the moutain")
                print("GAME OVER")

#Todo: End of The Game

        elif action == "run":
            print("You run away from the caveman and now you are lost in the cave.")
            print("GAME OVER")
        else:
            print("Invalid choice. The caveman claims the treasure map and hides it in the cave.")
    elif action == "back":
        print("You run away from the cave and now you are back in the village.")
        print("GAME OVER")
    else: 
        print("Invalid choice. You slip from the mountain trail and hurt yourself")
        print("GAME OVER")

else: print("Invalid Choice. GAME OVER")
