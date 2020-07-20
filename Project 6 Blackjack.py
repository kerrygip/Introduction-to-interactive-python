#Kerry's Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

# define hand class
class Hand:
    def __init__(self):
        self.card = []

    def __str__(self):
        stats = 'Hand contains '
        for i in self.card:
            stats = stats + str(i.__str__() + ' ')
        return stats

    def add_card(self, card):
        self.card.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        count = 0
        for i in self.card:
            count = count + VALUES[i.get_rank()]
        for i in self.card:
            if i.rank == 'A' and (count + 10 <= 21):
                count = count + 10
                    
        return count

    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for i in range(0, len(self.card)):
            self.card[i].draw(canvas, [pos[0] + i * CARD_SIZE[0]*1.1, pos[1]])

# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for rank in RANKS:
            for suit in SUITS:
                self.deck.append(Card(suit, rank))


    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()  

    def __str__(self):
        return "Deck constains " + str(deck)

#define event handlers for buttons
def deal():
    global outcome, in_play, player, dealer, score, deck
    if in_play == True:
        score -= 1
    in_play = True
    deck = Deck().shuffle
    player = Hand()
    dealer = Hand()
    deck = Deck()
    deck.shuffle()
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    outcome = "Hit or stay?" #stand?

def hit(): # how to do double down
    global in_play, player, deck, outcome, score	
    # replace with your code below
    
    if in_play:
        player.add_card(deck.deal_card())
        print "Player: " + str(player)
    # if the hand is in play, hit the player
    
    if player.get_value() > 21:
        print "Player: " + str(player)
        outcome = "Player busted. Dealer wins"
        score = score - 1
        
    elif player.get_value() == 21: 
        print "Player: Blackjack!"
        score = score + 1
        
def double_down():
    pass

def stand():
    global score, in_play, player, dealer, deck, outcome
    # replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer.get_value() <= 17:
            dealer.add_card(deck.deal_card())
            print "Dealer: " + str(dealer)
    
    # assign a message to outcome, update in_play and score
    if dealer.get_value > 21:
        in_play = False
        print "Dealer: " + str(dealer.get_value())
        outcome = "Dealer busted. Player wins"
        score = score + 1
        
    else:
        if  21 < dealer.get_value() > player.get_value():
            in_play = False
            print "Dealer: " + str(dealer.get_value())
            print "player: " + str(player.get_value())
            outcome = "Dealer wins"
            score = score - 1
        elif dealer.get_value() == player.get_value():
            in_play = False
            print "Dealer: " + str(dealer.get_value())
            print "Player: " + str(player.get_value())
            outcome = "Tie"
            score = score
        elif dealer.get_value() < player.get_value(): 
            in_play = False
            print "Dealer: " + str(dealer.get_value())
            print "Player: " + str(player.get_value())
            outcome = "Player wins"
            score = score + 1

def reset():
    global outcome, in_play, player, dealer, score, deck
    if in_play == True:
        score -= 1
        score = 0
    in_play = True
    deck = Deck().shuffle
    player = Hand()
    dealer = Hand()
    deck = Deck()
    deck.shuffle()
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    outcome = "Hit or stand?"
            

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below #after some score, all labels go away
    #if in_play == True: #has the current count - disappears when not in play anymore
    #keep this part on at all times 
    canvas.draw_text("Blackjack" , [150,60], 76 , "Black")
    canvas.draw_text("Score: " + str(score), [500,30], 24, "Black")	
    canvas.draw_text("Player: " + str(player.get_value()),[100,300], 24,"Black")
    canvas.draw_text("Dealer: " + str(dealer.get_value()), [100,100], 24,"Black")
    dealer.draw(canvas, [50,125])
    player.draw(canvas, [50,315])  


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Reset", reset, 200)
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.add_button("Double Down", double_down, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()