
'''
Given a root of a BST and a key find the next element of the key in BST
'''

import math

class Node:
   def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None

def nextElement(root, key):
   nextElem = None
   subtree = root

   while subtree:
      if key < subtree.value:
         nextElem = subtree
         subtree = subtree.left
      else:
         subtree = subtree.right
   
   return nextElem.value if nextElem else -1


def main():
   root = Node(25)
   root.left = Node(20)
   root.right = Node(36)

   root.left.left = Node(10)
   root.left.right = Node(22)
   root.right.left = Node(30)
   root.right.right = Node(40)

   root.left.left.left = Node(5)
   root.left.left.right = Node(12)
   root.right.left.left = Node(28)
   root.right.right.left = Node(38)
   root.right.right.right = Node(48)

   root.left.left.left.left = Node(1)
   root.left.left.left.right = Node(8)
   root.left.left.right.right = Node(15)
   root.right.right.right.left = Node(45)
   root.right.right.right.right = Node(50)

   print(nextElement(root,25))


if __name__ == "__main__":
   main()