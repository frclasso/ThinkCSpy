#!/usr/bin/python

previous = {0:1, 1:1}


def fibonacci(n):
    if previous.has_key(n):  #python2
        return previous[n]
    else:
        newValue = fibonacci(n-1) + fibonacci(n -2)
        previous[n] = newValue
        return newValue

fibonacci(4)