#!/usr/bin/pyton

#-*-coding: utf-8 -*-


class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

    def total(self, tree):
        if tree == None: return
        return total(tree.left) + total(tree.right) + tree.cargo

    def printTree(tree):
        if tree == None: return
        print (tree.cargo)
        Tree.printTree(tree.left)
        Tree.printTree(tree.right)

    def printTreePostOrder(tree):
        if tree == None: return
        Tree.printTreePostOrder(tree.left)
        Tree.printTreePostOrder(tree.right)
        print (tree.cargo),

    def printTreeInorder(tree):
        if tree == None: return
        Tree.printTreeInorder(tree.left)
        print(tree.cargo),
        Tree.printTreeInorder(tree.right)

    def printTreeIndented(tree,  level=0):
        if tree == None: return
        Tree.printTreeIndented(tree.right, level+1)
        print (' '*level + str(tree.cargo))
        Tree.printTreeIndented(tree.left, level+1)

    def getToken(tokenList, expected):
        if tokenList[0] == expected:
            del tokenList[0]
            return True
        else:
            return False

    def getNumber(tokenList):
        if Tree.getToken(tokenList, '('):
            x = Tree.getSum(tokenList) # get the subexpression
            Tree.getToken(tokenList, ')')
            return x
        else:
            x = tokenList[0]
            if not isinstance(x, int): return None
            tokenList[0:1] = []
            return Tree(x, None, None)

    def getProduct(tokenList):
        a = Tree.getNumber(tokenList)
        if Tree.getToken(tokenList, '*'):
            b = Tree.getProduct(tokenList) #this line changed
            return Tree('*', a, b)
        else:
            return a

    def getSum(tokenList):
        a = Tree.getProduct(tokenList)
        if Tree.getToken(tokenList, '+'):
            b = Tree.getSum(tokenList)
            return Tree('+', a, b)
        else:
            return a


"""
tokenList = [9, 11, 'end']
x = Tree.getNumber(tokenList)
Tree.printTreePostOrder(x)
print(tokenList)

print('---------------')
tokenList = [9, '*',  11, 'end']
tree = Tree.getProduct(tokenList)
Tree.printTreePostOrder(tree)


print('----------------')
tokenList = [9, '+',  11, 'end']
tree = Tree.getProduct(tokenList)
Tree.printTreePostOrder(tree)

print('----------------')
tokenList = [2, '*', 3, '*', 5, '*', 7, 'end']
tree = Tree.getProduct(tokenList)
Tree.printTreePostOrder(tree)

print('--------getSum--------')
tokenList = [9, '*', 11, '+', 5, '*', 7, 'end']
tree = Tree.getSum(tokenList)
Tree.printTreePostOrder(tree)

print('---------getNumber-------')
tokenList = [9, '*', '(', 11, '+', 5, ')', '*', 7, 'end']
tree = Tree.getSum(tokenList)
Tree.printTreePostOrder(tree)"""
