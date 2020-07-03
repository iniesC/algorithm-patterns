

'''
Given a root of a binary tree flatten the tree
'''


class Node:
   def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None


def _flatten_tree(root):
   if not root:
      return None
   
   if root.left is None and root.right is None:
      return root
   
   leftTail = _flatten_tree(root.left)
   rightTail = _flatten_tree(root.right)

   if leftTail:
      leftTail.right = root.right
      root.right = root.left
      root.left = None
   
   return rightTail if rightTail else leftTail

def flatten_tree(root):
   if not root:
      return None
   
   _flatten_tree(root)

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

   node = flatten_tree(root)
   while node:
      print(node.value, end=" ")

      node = node.right



if __name__ == "__main__":
   main()
