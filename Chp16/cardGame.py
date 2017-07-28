#!/usr/bin/python

#-*-coding: latin1-*-

from cards import Deck
from hand import Hand


class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()


class OldMaidHand(Hand):
    def removeMatches(self):
        count = 0
        originalCards = self.cards[:]
        for card in originalCards:
            match = Card(3 - card.suit, card.rank)
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)
                print("Hand %s: %s matches %s  " % (self.name,card, match))
                count = count + 1
        return count


#game = CardGame()
#hand = OldMaidHand("Frank Jessie")
#game.deck.deal([hand], 13)
#print(hand)

#hand.removeMatches()
#print(hand)