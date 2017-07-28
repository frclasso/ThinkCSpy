#!/usr/bin/python

import math


def printMultiples(n,  high):
    i = 1
    while i <= high:
        print(n * i, '\t', end='')
        i = i + 1
    print


def printMultTable(high):
    i = 1
    while i <= high:
        printMultiples(i, high)
        i = i + 1
    print


printMultiples(2, 6)
print()
printMultTable(6)