# Kerrys Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
score1 = 0
score2 = 0
ball_vel1 = 0
ball_vel2 = 0


# left game = WASD or some keys - paddle 1
#right game = up and down on same keyboard paddle 2

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    #random
    ball_pos=[WIDTH/2,HEIGHT/2]
    if(direction):
        ball_vel=[random.randrange(120,240)//60,-random.randrange(60,180)//60] #velocity per second - //60
    else:
        ball_vel=[-random.randrange(120,240)//60,-random.randrange(60,180)//60]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_pos = (HEIGHT/2)
    paddle2_pos = (HEIGHT/2)
    paddle1_vel = 0
    paddle2_vel = 0
    spawn_ball(RIGHT) #RANDRANGE THIS?
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]        
    
    # collide and reflect off of canvas - top, bottom, left, right 
    # determine whether paddle and ball collide
    #both paddles will roll through the bottom and ball
    
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
             
    
    if ball_pos[0] >= (WIDTH - BALL_RADIUS - PAD_WIDTH):
        if paddle2_pos <= ball_pos[1] <= (paddle2_pos+PAD_HEIGHT):
            ball_vel[0] = - 1.1 * ball_vel[0]
        else:
            spawn_ball(LEFT)
            score1 = score1+ 1
        
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if paddle1_pos <= ball_pos[1] <= (paddle1_pos+PAD_HEIGHT):
            ball_vel[0] = - 1.1 * ball_vel[0]
        else:
            spawn_ball(RIGHT)
            score2 = score2 +1
          
        
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos+= paddle1_vel
    paddle2_pos+= paddle2_vel
    
    if paddle1_pos <= 0:
        paddle1_pos = 0
    elif(paddle1_pos>= HEIGHT + PAD_HEIGHT): 
        paddle1_pos = HEIGHT + PAD_HEIGHT
        
    if paddle2_pos <= 0:
        paddle2_pos = 0
    elif(paddle1_pos>= HEIGHT - PAD_HEIGHT):
        paddle2_pos = HEIGHT - PAD_HEIGHT    
    
    # draw paddles - Left and Right Paddle
    canvas.draw_polygon([(0,paddle1_pos),(0,paddle1_pos+PAD_HEIGHT)],PAD_WIDTH*2,"White")    
    canvas.draw_polygon([(WIDTH,paddle2_pos),(WIDTH,paddle2_pos+PAD_HEIGHT)],PAD_WIDTH*2,"White")

    
                   
            
    # draw scores
    canvas.draw_text(str(score1),(20,30), 36, "Red")
    canvas.draw_text(str(score2),(550,30), 36, "Red")
       
    
    
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos
    if key == simplegui.KEY_MAP["w"]:
         paddle1_vel = paddle1_vel -3
    elif key == simplegui.KEY_MAP["s"]:
         paddle1_vel = paddle1_vel + 3
    elif key == simplegui.KEY_MAP["up"]:
         paddle2_vel = paddle2_vel -3 
    elif key == simplegui.KEY_MAP["down"]:
         paddle2_vel = paddle2_vel +3  
            
            
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset Game", new_game, 100)


# start frame
new_game()
frame.start()












#Someone Elses Game


# (# Implementation of classic arcade game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
score1 = 0
score2 = 0

#paddle position
paddle1_pos = HEIGHT/2 
paddle2_pos = HEIGHT/2

#paddle velocity
paddle1_vel = 0
paddle2_vel = 0

# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos = [WIDTH/2 , HEIGHT/2]
ball_vel = [0 , 0]

#set color theme
color_palette = ['#FF5252','#00BCD4','#536DFE','#8BC34A','#FFC107','#FF9800','#FF4081','#E040FB']

color = random.choice(color_palette)

def color_red():
    color = color_palette[0]

def color_l_blue():
    color = color_palette[1]

def color_d_blue():
    color = color_palette[2]

def color_green():
    color = color_palette[3]

def color_yellow():
    color = color_palette[4]

def color_orange():
    color = color_palette[5]

def color_pink():
    color = color_palette[6]

def color_purple():
    color = color_palette[7]

def open_game():
    global ball_pos, ball_vel
    ball_pos = [WIDTH/2 , HEIGHT/2]
    ball_vel[0] = 0
    ball_vel[1] = 0

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def start_game(direction):
    global ball_pos, ball_vel
    ball_pos = [WIDTH/2 , HEIGHT/2]

    if direction == RIGHT:
        ball_vel[0] = random.randrange(120,240)/60.0
        ball_vel[1] = -random.randrange(60,180)/60.0

    if direction == LEFT:
        ball_vel[0] = -random.randrange(120,240)/60.0
        ball_vel[1] = -random.randrange(60,180)/60.0

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2  
    paddle1_pos = HEIGHT/2  
    paddle2_pos = HEIGHT/2 
    open_game()
    score1 = 0
    score2 = 0

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_vel, paddle2_vel, PAD_HEIGHT, PAD_WIDTH, BALL_RADIUS,HALF_PAD_HEIGHT, HALF_PAD_WIDTH
    global color_palette, color

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    #ball with upper and lower wall collisions
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[0] = ball_vel[0]
        ball_vel[1] = -ball_vel[1]
    if ball_pos[1] >= (HEIGHT-1)-BALL_RADIUS:
        ball_vel[0] = ball_vel[0]
        ball_vel[1] = -ball_vel[1]

    #spawn ball left or right    
    if ball_pos[0] <= BALL_RADIUS+PAD_WIDTH:
        start_game(RIGHT)
        score2 += 1
    if ball_pos[0] >= (WIDTH-1)-PAD_WIDTH-BALL_RADIUS:
        start_game(LEFT)
        score1 += 1

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, color, color)

    #keep paddle on the screen
    if paddle1_pos-HALF_PAD_HEIGHT <= 0 and paddle1_vel < 0:
        paddle1_vel = 0
    if paddle2_pos-HALF_PAD_HEIGHT <= 0 and paddle2_vel < 0:
        paddle2_vel = 0
    if paddle1_pos+HALF_PAD_HEIGHT >= HEIGHT and paddle1_vel > 0:
        paddle1_vel = 0
    if paddle2_pos+HALF_PAD_HEIGHT >= HEIGHT and paddle2_vel > 0:
        paddle2_vel = 0

    # update paddle's vertical position 
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel

    # draw paddles
    canvas.draw_polygon([(0,paddle1_pos-HALF_PAD_HEIGHT),(PAD_WIDTH,paddle1_pos-HALF_PAD_HEIGHT),(PAD_WIDTH,paddle1_pos+HALF_PAD_HEIGHT),(0,paddle1_pos+HALF_PAD_HEIGHT)], 5, color, color)
    canvas.draw_polygon([(WIDTH,paddle2_pos-HALF_PAD_HEIGHT),(WIDTH-PAD_WIDTH,paddle2_pos-HALF_PAD_HEIGHT),(WIDTH-PAD_WIDTH,paddle2_pos+HALF_PAD_HEIGHT),(WIDTH,paddle2_pos+HALF_PAD_HEIGHT)], 5, color, color)

    # determine whether paddle and ball collide    
    if ball_pos[1] > paddle1_pos-HALF_PAD_HEIGHT -2 and ball_pos[1]<paddle1_pos +HALF_PAD_HEIGHT +2 and ball_pos[0] - BALL_RADIUS <= PAD_WIDTH+2:
        ball_vel[0] = -ball_vel[0]
        ball_vel[1] = ball_vel[1]

    if ball_pos[1] > paddle2_pos-HALF_PAD_HEIGHT -2 and ball_pos[1] < paddle2_pos +HALF_PAD_HEIGHT+2 and WIDTH - (WIDTH - (ball_pos[0] + BALL_RADIUS)) >= (WIDTH - PAD_WIDTH) -2:
        ball_vel[0] = -ball_vel[0]
        ball_vel[1] = ball_vel[1] 

    # draw scores
    canvas.draw_text(str(score1), (WIDTH/2 - 100,80), 60, color, 'sans-serif')
    canvas.draw_text(str(score2), (WIDTH/2 + 60,80), 60, color, 'sans-serif')

def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -4
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 4
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = -4
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 4
    elif key == simplegui.KEY_MAP['space']:
        start_game(random.choice([LEFT,RIGHT]))

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_canvas_background('#192c36')
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_label('Start the game by pressing SPACE'),frame.add_label(' ')
frame.add_button('Restart', new_game, 100),frame.add_label(' ')
frame.add_label('Choose color theme: '),frame.add_label(' ')
frame.add_button('Red', color_red, 100)
frame.add_button('Light Blue', color_l_blue, 100)
frame.add_button('Dark Blue', color_d_blue, 100)
frame.add_button('Green', color_green, 100)
frame.add_button('Yellow', color_yellow, 100)
frame.add_button('Orange', color_orange, 100)
frame.add_button('Pink', color_pink, 100)
frame.add_button('Purple', color_purple, 100)


# start frame
open_game()
frame.start())

