
'''
Problem Statement #
Given a binary tree where each node can only have a digit (0-9) value, 
each root-to-leaf path will represent a number. 
Find the total sum of all the numbers represented by all paths.
'''
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def find_sum_of_path_numbers(root):
   def helper(root,sum):
      if not root:
         return 0
      
      sum = sum * 10 + root.val

      if root.left is None and root.right is None:
         return sum
      
      return helper(root.left, sum) + helper(root.right, sum)
   
   return helper(root, 0)


def main():
   root = TreeNode(1)
   root.left = TreeNode(0)
   root.right = TreeNode(1)
   root.left.left = TreeNode(1)
   root.right.left = TreeNode(6)
   root.right.right = TreeNode(5)
   print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))

if __name__ == "__main__":
   main()

