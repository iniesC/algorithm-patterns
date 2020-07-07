
'''
Problem Statement #
Given a binary tree and a number ‘S’, find all paths 
in the tree such that the sum of all the node values of each path equals ‘S’. 
Please note that the paths can start or end at any node but all paths must 
follow direction from parent to child (top to bottom).
'''
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def count_paths(root, sum):

   def helper(root, curr_path):
      if not root:
         return 0
      
      cnt = 0
      curr_path.append(root.val)
      path_sum = 0
      for i in range(len(curr_path)-1, -1, -1):
         path_sum += curr_path[i]
         if path_sum == sum:
            cnt += 1 
      
      if root.left is None and root.right is None:
         return cnt
      
      cnt += helper(root.left, curr_path)
      cnt += helper(root.right, curr_path)

      del curr_path[-1]

      return cnt

   return helper(root, [])

def main():
   root = TreeNode(12)
   root.left = TreeNode(7)
   root.right = TreeNode(1)
   root.left.left = TreeNode(4)
   root.right.left = TreeNode(10)
   root.right.right = TreeNode(5)
   print("Tree has paths: " + str(count_paths(root, 11)))

if __name__ == "__main__":
   main()

