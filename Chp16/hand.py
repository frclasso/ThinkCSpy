#!/usr/bin/python

# -*- coding: latin1 -*-

#from Chp15.cards import Deck
from Chp16.cards import Deck


class Hand(Deck):
    def __init__(self, name=""):
        super(Hand, self).__init__()
        self.cards = []
        self.name = name

    def addCard(self, card):
        self.cards.append(card)

    def __str__(self):
        s = "Hand " + self.name
        if self.isEmpty():
            return s + " is empty\n"
        else:
            return s + " contains: \n" + Deck.__str__(self)

#deck = Deck()
#deck.shuffle()
#hand = Hand("Frank")
#deck.deal([hand], 5)
#print(hand)