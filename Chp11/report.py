#!/usr/bin/python

#-*- coding: utf-8 -*-


def report(wages):
    students = wages.keys()
    students.sort()
    for student in students:
        print ('%-20s %12.2f' % (student, wages[student]))

wages = {'Mary': 6.23, 'Joe': 4.25, 'Joshua Red Man': 4.25}
report(wages)