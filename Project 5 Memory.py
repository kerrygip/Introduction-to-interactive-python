#Kerry's implementation of card game - Memory

import simplegui
import random
import math


#Variables
turn = 0
state = 0
card1 = 0
card2 = 0
duel = []


# helper function to initialize globals - created the the deck here instead in decklist
def new_game():
    global turn, state, duel, exposed
    
    turn = 0
    deck1 = range(0,8)
    deck2 = range(0,8)
    duel = deck1 + deck2
    exposed = [False for card in range(len(duel))]
   
    random.shuffle(duel)
    


          
# define event handlers 
def mouseclick(pos):
    # add game state logic here
    global state, turn, duel,exposed, card1, card2
    
    click = pos[0]/50 #card space
    #but now clicks will pair up the two. how to separate them?
    if not exposed[click]:
        exposed[click]= True
        
        if state == 0:
            state = 1
            card1= click
        elif state == 1:
            state = 2
            card2 = click
            turn = turn + 1
            label.set_text("Turns = "+ str(turn))  
            
        elif state==2:
            if duel[card1] != duel[card2]:
                exposed[card1] = False
                exposed[card2] = False
            state = 1
            card1 = click
            
        
        
      
    
# cards are logically 50x100 pixels in size  
def draw(canvas):
    global duel
    count = 0
    click = 0
    
    for click in range(len(duel)):
        if not exposed[click]:
            canvas.draw_polygon([(count,0),(count,100),(count+50,100),(count+50,0)], 
                                  2, "Black", "Pink")
            

        else: #shows the number of the card/ exposed
            
            canvas.draw_text(str(duel[click]),(count,100),64, "White")
            frame.set_canvas_background("Blue")
        count = count+50       
        click = click+1
        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(turn))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric