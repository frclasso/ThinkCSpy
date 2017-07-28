#!/usr/bin/python

#-*- coding: utf-8 -*-


class Point:
    def __init__(self, x=0, y=0):
        self.x =x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def __add__(self, other):
        return Point(self.x + other.x,  self.y + other.y)

    def __mul__(self, other):
        return self.x * other.x , self.y * other.y

    def __rmul__(self, other):
        return Point(other * self.y, other * self.y)




p = Point(3, 4)
print(p)

p1 = Point(3, 4)
p2 = Point(5, 7)
p3 = p1 + p2
print(p3)
print(p1 * p2)
print(2 * p2)
