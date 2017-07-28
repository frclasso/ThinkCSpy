#!/usr/bin/python

#-*- coding: latin1 -*-


def find(str, ch):
    index = 0
    while index < len(str):
        if str[index] == ch:
            return index
        index = index + 1
    return -1
