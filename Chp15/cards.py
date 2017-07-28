#!/usr/bin/python

#-*-coding: latin1-*-


class Card:

    suitList = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rankList = ['narf', 'Ace', '2', '3', '4', '5', '6', '7',
                '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.rankList[self.rank] + ' of ' +
                self.suitList[self.suit])

    def __cmp__(self, other):
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        return 0


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def printDeck(self):
        for card in self.cards:
            print(card)

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " "*i + str(self.cards[i]) + "\n"
        return s

    def shuffle(self):
        import random
        nCards = len(self.cards)
        for i in range(nCards):
            j = random.randrange(i, nCards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def removeCard(self, card):
        if card in self.cards:
            self.cads.remove(card)
            return True
        else:
            return False

    def popCard(self):
        return self.cards.pop()

    def isEmpty(self):
        return (len(self.cards) == 0)

    def deal(self, hands, nCards=999):
        nHands = len(hands)
        for i in range(nCards):
            if self.isEmpty():
                break  #break if out of cards
            card = self.popCard() #take the top card
            hand = hands[i % nHands]
            hand.addCard(card)  #addd the card to the hand


"""card1 = Card(1, 11)  #suitList element (Diamonds) + rankList eleemnt (Jack = 11)
print(card1)

card2 = Card(1, 3)
print(card2)
print (card2.suitList[1])

deck = Deck()
print(deck)"""

