#!/usr/bin/python

#-*- coding: utf-8 -*-
from Chp19.Queue import *

class Golfer:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return "%-16s: %d" % (self.name, self.score)

    def __cmp__(self, other):
        if self.score < other.score: return 1
        if self.score > other.score: return -1

tiger = Golfer("Tiger Woods", 61)
phil = Golfer("Phil Mickelson", 72)
hal = Golfer("Hal Sutton", 69)

pq = PriorityQueue()
pq.insert(tiger)
pq.insert(phil)
pq.insert(hal)

while not pq.isEmpty(): print(pq.remove())