#!/usr/bin/python


def factorial(n):
    if not isinstance(n, int):
        print("Factorial is only defined for integers")
        return -1
    elif n < 0:
        print("Factorial is only defined for positive integers")
    elif n == 0 :
        return 1
    else:
        return n * factorial(n-1)

