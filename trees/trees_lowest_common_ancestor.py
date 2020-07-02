

'''
Given a root of a binary tree and value X and Y find the lowest common ancestor
'''


class Node:
   def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None

def findLCA(root, X, Y):
   if not root:
      return None
   
   if root.value == X or root.value == Y:
      return root
   
   left = findLCA(root.left, X, Y)
   right = findLCA(root.right, X, Y)

   if not left:
      return right
   if not right:
      return left
   
   return root


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

   lca_node = findLCA(root,9,15)
   if lca_node:
      print(lca_node.value)


if __name__ == "__main__":
   main()
