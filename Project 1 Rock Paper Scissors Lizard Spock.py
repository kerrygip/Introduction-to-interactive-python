#Kerry's Mini Project #1 Rock/Paper/Scissors/Lizard/Spock

import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    pass

    # convert name to number using if/elif/else
    # don't forget to return the result!
def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Error"

def number_to_name(number):
    # delete the following pass statement and fill in your code below
    pass
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
def number_to_name(num):
    if num == 0:
        return "rock"
    elif num == 1:
        return "Spock"
    elif num == 2:
        return "paper"
    elif num == 3:
        return "lizard"
    elif num == 4:
        return "scissors"
    else:
        return "Error"  
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    
    # print a blank line to separate consecutive games
    print " "
    # print out the message for the player's choice
    print "Player chooses " + player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number= name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print "Comp chooses " + comp_choice 
    # compute difference of comp_number and player_number modulo five
    diff =int(comp_number) - int(player_number)%5
    # use if/elif/else to determine winner, print winner message
    if diff ==3:
        print "It's a tie!"
    if diff < 3: 
        print "Comp wins"
    else:
        print "You win"
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


