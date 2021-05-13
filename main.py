# ==================================================== #
#                                                      #
#  Created By: Darhil Aslaliya -  GitHub :- darsh-22   #
#                                                      #
# ==================================================== #

# required module
import random

# main function
def game(usr_choice, comp_choice):

    # if computer choise and user choice is same return tie message
    if comp_choice == usr_choice:
        print("####################################")
        print("##                                ##")
        print("## Match tied!! Sharp mind huh ;) ##")
        print("##                                ##")
        print("####################################")

    # if user choise is rock
    elif usr_choice == 1:
        # and if computer choise is scissor disply lose message
        if comp_choice == 2:
            print("########################")
            print("##                    ##")
            print("## Oouch!! You loose! ##")
            print("##                    ##")
            print("########################")
        # and if computer choise is paper disply won message
        elif comp_choice == 3:
            print("###############################")
            print("##                           ##")
            print("## Well well well!! You won! ##")
            print("##                           ##")
            print("###############################")

    # if user choise is paper
    elif usr_choice == 2:
        # and if computer choise is scissor disply lose message
        if comp_choice == 3:
            print("########################")
            print("##                    ##")
            print("## Oouch!! You loose! ##")
            print("##                    ##")
            print("########################")
        # and if computer choise is rock disply won message
        elif comp_choice == 1:
            print("###############################")
            print("##                           ##")
            print("## Well well well!! You won! ##")
            print("##                           ##")
            print("###############################")

    # if user choise is scissor    
    elif usr_choice == 3:
        # and if computer choise is paper disply won message
        if comp_choice == 2:
            print("###############################")
            print("##                           ##")
            print("## Well well well!! You won! ##")
            print("##                           ##")
            print("###############################")
        # and if computer choise is rock disply lose message
        elif comp_choice == 1:
            print("########################")
            print("##                    ##")
            print("## Oouch!! You loose! ##")
            print("##                    ##")
            print("########################")

# driver code for rock paper scissor game
while True:
    # defining all possibilites of rock paper scissor game
    possibilites = [1,2,3]
    print("Rock (1) Paper (2) Scissors (3)")
    
    # user choice of rock paper scissor game
    usr_choice = int(input("Enter your choice: "))
    if usr_choice == 1:
        print(f"You chose {usr_choice} Rock")
    elif usr_choice == 2:
        print(f"You chose {usr_choice} Paper")
    elif usr_choice == 3:
        print(f"You chose {usr_choice} Scissor")

    # computer choice of rock paper scissor game
    comp_choice = random.choice(possibilites)
    
    if comp_choice == 1:
        print(f"Computer chose {comp_choice} Rock")
    elif comp_choice == 2:
        print(f"Computer chose {comp_choice} Paper")
    elif comp_choice == 3:
        print(f"Computer chose {comp_choice} Scissor")

    # check if user input is correct or not
    if usr_choice in possibilites:
        game(usr_choice,comp_choice)
    else:
        print("#########################################")
        print("##                                     ##")
        print("## Wait what!! You enter wrong choice! ##")
        print("##                                     ##")
        print("#########################################")
        break