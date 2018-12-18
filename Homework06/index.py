import simplegui
import random

CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")

in_play = False
outcome = ""
score = 0


SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
          '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}


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
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.idex(self.rank)
                    )(CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [
                          pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)


class Hand:
    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        handvalue = 0
        aces = 0
        for x in self.hand:
            if x.get_rank() == 'A':
                aces += 1
            handvalue += VALUES.get(x.get_rank())
        if aces > 0 and (handvalue + 10) <= 21:
            handvalue += 10
        return handvalue

    def draw(self, canvas, p):
        for z in self.hand:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(z.rank),
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(z.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [
                              p[0] + CARD_CENTER[0] + 73 * self.hand.index(z), p[1] + CARD_CENTER[1]], CARD_SIZE)

    def __str__(self):
        handstr = ''
        for x in self.hand:
            handstr = handstr + str(x)
        return handstr


class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(str(suit), str(rank)))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        self.card = self.deck[0]
        self.deck.remove(self.card)
        return self.card

    def __str__(self):
        handstr = ''
        for x in self.hand:
            handstr = handstr + str(x)
        return handstr


def deal():
    global outcome, in_play, deck, player_hand, dealer_hand, deck, score

    if(in_play == True):
        outcome = "You lose! New deal?"
        score -= 1
        in_play = False
    else:
        deck = Deck()
        outcome = "Hit or stand?"
        deck.shuffle()

        player_hand = Hand()
        dealer_hand = Hand()

        player_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())

        dealer_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())

        in_play = True


def hit():
    global outcome, score, in_play
    player_hand.add_card(deck.deal_card())
    if player_hand.get_value() > 21:
        outcome = "You have busted. New deal?"
        score -= 1
        in_play = False
        return score, outcome, in_play
    else:
        outcome = "Hit or stand?"


def restart():
    global score
    score = 0


def stand():
    global outcome, score, in_play
    in_play = False
    if player_hand.get_value() > 21:
        outcome = "You have busted. New deal?"
        score -= 1
        return score, outcome, in_play
    else:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
        else:
            if dealer_hand.get_value() > 21:
                outcome = "Dealer busts, you win. New deal?"
                score += 1
                return score, outcome, in_play
            elif dealer_hand.get_value() >= player_hand.get_value():
                outcome = "Dealer wins. New deal?"
                score -= 1
                return score, outcome, in_play
            else:
                outcome = "You win. New deal?"
                score += 1
                return score, outcome, in_play


def draw(canvas):
    global player, dealer

    canvas.draw_text('Blackjack or 21', [220, 60], 50, 'Black')
    canvas.draw_text('Score: '+str(score), [50, 50], 20, 'Black')
    canvas.draw_text(outcome, [10, 90], 20, 'Black')
    player_hand.draw(canvas, [0, 100])
    dealer_hand.draw(canvas, [0, 300])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [
                          0 + CARD_BACK_CENTER[0], 100 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)


frame = simplegui.create_frame("Blackjack", 600, 500)
frame.set_canvas_background("Green")


frame.add_button('Deal', deal, 200)
frame.add_button('Hit',  hit, 200)
frame.add_button('Stand', stand, 200)
frame.add_button('Restart', restart, 200)
frame.set_draw_handler(draw)

deal()
frame.start()
