#!/usr/bin/python

#-*-coding: utf-8 -*-

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def printBackward(self):
        print("["),
        if self.head != None:
            self.head.printBackward()
        print ("]"),

    def addFirst(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length = self.length + 1


class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

    def printList(node):
        while node:
            print(node),
            node = node.next
        print()

    def printBackward(self):
        """if list == None: return
        head = list
        tail = list.next
        printBackward(tail)
        print(head),"""
        if self.next != None:
            tail = self.next
            tail.printBackward()
        print (self.cargo),

    def removeSecond(list):
        if list == None: return
        first = list
        second = list.next
        first.next = second.next
        second.next = None
        return second
        


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

printListas = Node.printList(node1)
#backward = Node.printBackward(node1)


#printListas2 = None.printList(node1)

removed = Node.removeSecond(node1)
printListaRemoved = Node.printList(removed)

printLista = Node.printList(node1)