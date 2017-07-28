#!/usr/bin/python

#-*-coding: utf-8 -*-


class Queue:
    def __init__(self):
        self.length = 0
        self.head = None

    def isEmpty(self):
        return (self.length == 0)

    def insert(self, cargo):
        node = Node(cargo)
        node.next = None
        if self.head == None:
            #if list is empty the new node goes first
            self.head = node
        else:
            #find the last node int the list
            last  = self.head
            while last.next: last = last.next
            #append the new node
            last.next = node
        self.length = self.length + 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length = self.length -1
        return cargo


class ImprovedQueue:

    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def isEmpty(self):
        return (self.length == 0)

    def insert(self, cargo):
        node = Node(cargo)
        node.next = None
        if self.length == 0:
            #if list is empty, the new node is head and last
            self.head = self.last = node
        else:
            #find the last node
            last = self.last
            #append the new node
            last.next = node
            self.last = node
        self.length = self.length + 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length = self.length - 1
        if self.length == 0:
            self.last = None
        return cargo


class PriorityQueue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        item = self.items[maxi]
        self.items[maxi:maxi + 1] = []
        return item

# q = PriorityQueue()
# q.insert(11)
# q.insert(12)
# q.insert(14)
# q.insert(13)
# while not q.isEmpty():print (q.remove())
