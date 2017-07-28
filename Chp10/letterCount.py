#!/usr/bin/python

#-*- coding: utf8 -*-

letterCounts = {}
for letter in 'Mississippi':
    letterCounts[letter] = letterCounts.get(letter, 0) + 1

print(letterCounts)

"""letterItems = letterCounts.items()
letterItems.sort() #python2
print(letterItems)"""