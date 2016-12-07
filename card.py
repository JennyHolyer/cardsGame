import random

# Class for card
class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def show(self):
        print self.value + " " + self.suit


# Class for Deck
class Deck(object):
    def __init__(self):
        self.cards = []
        self.get_cards()
        print "Deck is running!"

    def get_cards(self):
        # self.card = ''
        suit = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        rank = ['Ace', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        for i in suit:
            for j in rank:
                newcard = Card(j, i)
                self.cards.append(newcard)

    def show(self):
        for card in self.cards:
            card.show()
            # print card.value + " " + card.suit

    def shuffle(self):
        random.shuffle(self.cards)
        print "Shuffle is running!"

    def deal(self):
        return self.cards.pop()

# Class for Player
class Player(object):
    def __init__(self, name):
        self.hand = []
        self.name = name

    def discard(self):
        print "Discard is running!"

    def draw_cards(self, number, deck):
        if number <= len(deck.cards):
            for i in range (number):
                dealtcard = deck.deal()
                self.hand.append(dealtcard)
                # print "Draw Cards running!"

    def show(self):
        for card in self.hand:
            card.show()

        print "Show is running!"

# Test
# card = Card('7', 'Hearts') # Ask about quotes
newdeck = Deck()
newdeck.shuffle()
tim = Player('timo')
tim.draw_cards(6, newdeck)
tim.show()
# dealtcard = newdeck.deal()
# dealtcard2 = newdeck.deal()
# dealtcard3 = newdeck.deal()
# dealtcard.show()
# dealtcard2.show()
# dealtcard3.show()
