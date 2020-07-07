

'''
Given a root of a binary tree traverse the vertically from left to right
'''
from collections import deque

class Node:
   def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None


def preorder(root):
   if not root:
      return None
   
   stack = []
   stack.append(root)
   result = []
   while stack:
      n = stack.pop()
      result.append(n.value)

      if n.right:
         stack.append(n.right)
      if n.left:
         stack.append(n.left)
   
   return result

def inorder(root):
   if not root:
      return None

   result = []
   stack = []

   while True:

      while root:
         stack.append(root)
         root = root.left
      
      if len(stack) == 0:
         break

      n = stack.pop()
      result.append(n.value)

      if n.right:
         root = n.right
   
   return result



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

   print("Preorder Traversal: ", preorder(root))

   print("Inorder Traversal: ", inorder(root))

if __name__ == "__main__":
   main()
