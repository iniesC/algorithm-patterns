

'''
Cloning linkedlist, tree, and graph
'''

class Node:
   def __init__(self, value):
      self.value = value
      
      #tree
      self.left = None
      self.right = None

      #list
      self.next = None

      #random pointer
      self.random = None


def clone_list(head):

   created_node = {}

   def helper(head):
      if not head:
         return None
      
      if head in created_node:
         return created_node[head]
      
      node = Node(head.value)

      created_node[head] = node

      node.next = helper(head.next)

      return node
   
   return helper(head)

def clone_random_list(head):

   created_node = {}

   def helper(head):
      if not head:
         return None
      
      if head in created_node:
         return created_node[head]
      
      node = Node(head.value)

      created_node[head] = node

      node.next = helper(head.next)
      node.random = helper(head.random)

      return node
   
   return helper(head)


def clone_tree(root):

   cloned_node = {}

   def helper(root):
      if not root:
         return None
      
      if root in cloned_node:
         return cloned_node[root]
      
      node = Node(root.value)

      cloned_node[root] = node

      node.left = helper(root.left)
      node.right = helper(root.right)

      return node
   
   return helper(root)

def preorder(root):
   if not root:
      return
   
   print(root.value, end=" ")

   preorder(root.left)
   preorder(root.right)

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

   preorder(root)
   # print("\n")

   # cloned_root = clone_tree(root)

   # preorder(cloned_root)

   #list

   head = Node(7)
   head.next = Node(13)
   head.next.next = Node(11)
   head.next.next.next = Node(10)
   head.next.next.next.next = Node(1)

   cloned_list = clone_list(head)

   temp = cloned_list
   while temp:
      print(temp.value, end=" ")
      temp = temp.next
   print("\n")

   cloned_random_list = clone_random_list(head)
   temp = cloned_random_list
   while temp:
      print(temp.value, end=" ")
      temp = temp.random
   print("\n")





if __name__ == "__main__":
   main()
