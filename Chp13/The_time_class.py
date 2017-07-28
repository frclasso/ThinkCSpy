#!/usr/bin/python

#-*- coding: utf-8 -*-


class Time:

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def printTime(time):
        print(str(time.hours) + ":" + \
              str(time.minutes) + ":" + \
              str(time.seconds))

    def increment(self, seconds):
        self.seconds = seconds + self.seconds

        while self.seconds >= 60:
            self.seconds = self.seconds - 60
            self.minutes = self.minutes + 1

        while self.minutes >= 60:
            self.minutes = self.minutes - 60
            self.hours = self.hours + 1


time = Time()
time.hours = 11
time.minutes = 59
time.seconds = 30


def convertToSeconds(t):
    minutes = t.hours * 60 + t.minutes
    seconds = minutes * 60 + t.seconds
    return seconds


def makeTime(seconds):
    time = Time()
    time.hours = seconds // 3600
    time.minutes = (seconds % 3600)//60
    time.seconds = seconds % 60
    return time


def addTime(t1, t2):
    seconds = convertToSeconds(t1) + convertToSeconds(t2)
    return makeTime(seconds)


currentTime = Time()
currentTime.hours = 9
currentTime.minutes = 14
currentTime.seconds = 30

breadTime = Time()
breadTime.hours = 3
breadTime.minutes = 35
breadTime.seconds = 0

doneTime = addTime(currentTime, breadTime)

print('Current time', end=' => ')
currentTime.printTime()
print('Bread time', end=' => ')
breadTime.printTime()
print('Done time', end=' => ')
doneTime.printTime()
print('Current time incremented by 500', end=' => ')
currentTime.increment(500)
currentTime.printTime()

print('Current time (9, 14, 30)', end=" => ")
currentTime = Time(9, 14, 30)
currentTime.printTime()

print('Curremnt time (seconds = 30 and hours = 9)', end=' => ')
currentTime = Time(seconds=30, hours=9)
currentTime.printTime()
