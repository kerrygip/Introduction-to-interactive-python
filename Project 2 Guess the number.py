#Kerry Mini Project #2

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import math
import random

leftover = 7
num_range = 100
comp_guess = random.randrange(num_range)

print "Guess the number!"

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global num_range 
    global leftover
    comp_guess = random.randrange(0,num_range)
    if num_range == 100:
        leftover = 7
        print "You have 7 guesses"
    else:
        leftover = 10
        print "You have 10 guesses"
    print "New Game"
    print "Range is between 0 to " + str(num_range)
    print ""
   


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    global leftover
    num_range = 100
    print "Guess the number between 0-100"
    new_game()
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game   
    global num_range
    global leftover
    num_range = 1000
    print "Guess the number between 0-1000"
    new_game()
    
    
def input_guess(guess):
    # main game logic goes here	
    global num_range
    global leftover
    leftover -=1
    player_guess = int(guess)
  
    
    if (comp_guess == player_guess):
        print "You chose " + str(player_guess)
        print "Winner winner chicken dinner!"
        print "The secret number was " + str(comp_guess)
        print ""
        new_game()
    elif (comp_guess < player_guess and leftover >0):
        print "You chose " + str(player_guess)
        print "Lower" + " you have " + str(leftover) + " guesses left"
        print ""
    elif (comp_guess > player_guess and leftover >0):
        print "You chose " + str(player_guess)
        print "Higher" + " you have " + str(leftover) + " guesses left"
        print ""
    elif (leftover ==0):
        print "You chose " + str(player_guess)
        print "Game Over : You ran out of guesses"
        print "The secret number was " + str(comp_guess)
        new_game()
 

    

    
# create frame
f = simplegui.create_frame("Guess the number", 200,200)

# register event handlers for control elements and start frame
f.add_button("Range 0-100", range100, 200)
f.add_button("Range 0-1000", range1000, 200)
f.add_input("What's your guess?", input_guess, 100)
# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
