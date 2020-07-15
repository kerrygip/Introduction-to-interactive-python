#Kerrys Stopwatch project #3

# define global variables
import math
import simplegui

count = 0
games_played = 0
wins = 0
t=0 

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global count
    A= count//600
    B= (count//100)%6
    C= (count//10)%10
    D= count%10
    return str(A) + ":" + str(B) + str(C) + "." + str(D)

#minutes:seconds.tenths of a second A:BC.D
#needs to return
# define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    timer.start()
    
def stop():
    global games_played
    global wins
    timer.stop()
    games_played += 1
    
    if count%10 ==0:
        wins += 1
#have stop time match with x:xx.0    
def reset():
    global count
    global wins
    global games_played
    count= 0
    games_played = 0
    wins = 0
    
    
def score():
    global games_played
    global wins
    return "Score: " + str(wins) + "/" + str(games_played)
    
# define event handler for timer with 0.1 sec interval
def tick():
    global count
    count += 1
    return count

# define draw handler
def draw(canvas):
    canvas.draw_text(format(t),(90,150),48, "White")
    canvas.draw_text(score(),(0,30), 24, "Red")
                 
    
# create frame
frame = simplegui.create_frame("Timer Game", 300,300)
timer = simplegui.create_timer(100,tick)
frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# register event handlers


# start frame
frame.start()