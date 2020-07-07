

'''
Given a root of a binary tree traverse the vertically from left to right
'''
from collections import deque

class Node:
   def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None


def vertical_traversal(root):
   if not root:
      return None
   traverse_dict = {}
   q = deque()
   q.append((root, 0))

   while q:

      n, axis = q.popleft()
      if axis not in traverse_dict:
         traverse_dict[axis] = []
      traverse_dict[axis].append(n.value)

      if n.left:
         q.append((n.left, axis-1))
      if n.right:
         q.append((n.right, axis+1))
   
   return sorted(traverse_dict.values())


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

   print("Vertical Traversal: ", vertical_traversal(root))



if __name__ == "__main__":
   main()
