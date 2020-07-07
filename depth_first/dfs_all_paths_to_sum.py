
'''
Problem Statement #
Given a binary tree and a number ‘S’, 
find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.
'''

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def find_paths(root, sum):
   if root == None:
      return 0
   
   cnt = 0
   if root.val == sum and root.left is None and root.right is None:
      cnt += 1
   else:
      cnt += find_paths(root.left, sum-root.val)
      cnt += find_paths(root.right, sum-root.val)

   return cnt


def main():
   root = TreeNode(12)
   root.left = TreeNode(7)
   root.right = TreeNode(1)
   root.left.left = TreeNode(4)
   root.right.left = TreeNode(10)
   root.right.right = TreeNode(5)
   
   sum = 23
   print("Tree paths with sum " + str(sum) +
         ": " + str(find_paths(root, sum)))

if __name__ == "__main__":
   main()

