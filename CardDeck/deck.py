# deck.py

import card
from card import Card

import random
from random import shuffle

card.importTest()

class Deck:
    kind = 'deck'
    def __init__(self, typeOD):
        if typeOD == "true deck":
            self.buy()
        else:
            self.CLID = []

    def buy(self):
        cardList = []
        x = 1
        for i in range(1,14):
            cardList.append(Card("h",x))
            cardList.append(Card("d",x))
            cardList.append(Card("c",x))
            cardList.append(Card("s",x))
            x += 1
        self.CLID = cardList

    def show(self):
        if self.CLID == []:
            print("This deck empty, yeet.")
            return
        for i in self.CLID:
            i.showName()
        print("\n")

    def shuffleDeck(self):
        shuffle(self.CLID)
        print("\n")

    def draw(self):
        return self.CLID.pop(0)

    def addTake(self,victim):
        self.CLID.append(victim.draw())
        print("You draw a card...")

d = Deck("true deck")

d.shuffleDeck()

h = Deck("hand")
h.addTake(d)
print("Your hand has:")
h.show()
