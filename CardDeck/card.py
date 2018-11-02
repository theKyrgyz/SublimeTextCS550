# card.py

import random
from random import shuffle

def importTest():
    print("\ncard.py import successful.\n")

class Card:
    kind = 'card'
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def showSuit(self):
        if self.suit == "h":
            return "Hearts"
        if self.suit == "d":
            return "Diamonds"
        if self.suit == "c":
            return "Clubs"
        if self.suit == "s":
            return "Spades"
        else:
            return "N/A"

    def showRank(self):
        if self.rank == 1:
            return "Ace"
        if self.rank == 11:
            return "Jack"
        if self.rank == 12:
            return "Queen"
        if self.rank == 13:
            return "King"
        else:
            return self.rank

    def showName(self):
        return str(self.showRank())+" of "+self.showSuit()

TC1 = Card("h",3)

