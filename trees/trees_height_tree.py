

'''
Given a root of a binary tree flatten the tree
'''
from collections import deque

class Node:
   def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None

def tree_height(root):
   if not root:
      return 0
   
   return 1 + max(tree_height(root.left), tree_height(root.right))

def tree_height_min(root):
   if not root:
      return 0
   
   q = deque()
   q.append(root)

   ht = 0

   while q:
      qlen = len(q)

      ht += 1
      for _ in range(qlen):
         n = q.popleft()
      
         if n.left is None and n.right is None:
            return ht
      
         if n.left:
            q.append(n.left)
         if n.right:
            q.append(n.right)
   
   return ht

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

   print("Max height of the tree is : ", tree_height(root))
   print("Min height of the tree is : ", tree_height_min(root))





if __name__ == "__main__":
   main()
