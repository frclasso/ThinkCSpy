#!/usr/bin/python

#-*- coding: utf-8 -*-


class Fraction:
    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "%d/%d" % (self.numerator, self.denominator)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.numerator*other.numerator,
                        self.denominator * other.denominator)

    __rmul__ = __mul__

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.numerator * other.denominator +
                        self.denominator * other.numerator,
                        self.denominator * other.denominator)

    __radd__ = __add__