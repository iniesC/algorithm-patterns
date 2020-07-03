
'''
Given a root of a binary tree check if it is a BST
'''

import math

class Node:
   def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None

def _isBST(root, low, high):
   if not root:
      return True
   
   if root.value < low or root.value > high:
      print(low, root.value, high)
      return False
   
   return _isBST(root.left, low, root.value) and \
          _isBST(root.right, root.value, high)

def isBST(root):
   if not root:
      return False

   low = -math.inf
   high = math.inf

   return _isBST(root,low,high)

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

   print(isBST(root))


if __name__ == "__main__":
   main()