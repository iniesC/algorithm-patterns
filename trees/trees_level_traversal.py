

'''
Given a root of a binary tree flatten the tree
'''
from collections import deque

class Node:
   def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None

def levelTraversalV2(root):
   if not root:
      return
   
   q = deque()
   q.append(root)
   result = deque()

   while q:
      n = q.popleft()
      result.appendleft(n.value)

      if n.right:
         q.append(n.right)
      if n.left:
         q.append(n.left)
      
   return list(result)

def levelTraversal(root):
   if not root:
      return
   
   q = deque()
   q.append(root)
   result = []

   while q:
      qlen = len(q)

      temp = []
      for i in range(qlen):
         n = q.popleft()

         if n.left:
            q.append(n.left)
         if n.right:
            q.append(n.right)
         
         temp.append(n.value)
      result.append(list(temp))
   
   return result

def reverse_levelTraversal(root):
   if not root:
      return None
   
   q = deque()
   result = deque()

   q.append(root)

   while q:
      qlen = len(q)

      temp = []
      for _ in range(qlen):
         n = q.popleft()

         if n.left:
            q.append(n.left)
         
         if n.right:
             q.append(n.right)

         temp.append(n.value)
      
      result.appendleft(list(temp))

   return list(result)

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

   print("Reverse Level Traversing: ", levelTraversalV2(root))
   print("Level Traversing: ", levelTraversal(root))
   print("Reverse Level Traversing: ", reverse_levelTraversal(root))




if __name__ == "__main__":
   main()
