
'''
Tree Diameter (medium) #
Given a binary tree, find the length of its diameter. 
The diameter of a tree is the number of nodes on the longest 
path between any two leaf nodes. The diameter of a tree may or may not pass through the root.

Note: You can always assume that there are at least two leaf nodes in the given tree.
'''
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def find_diameter(root):
   max_diameter = 0

   def helper(root):
      nonlocal max_diameter

      if not root:
         return 0
      
      left_height = helper(root.left)
      right_height = helper(root.right)

      diameter = 1 + left_height + right_height

      max_diameter = max(max_diameter, diameter)

      return 1 + max(left_height, right_height)
   
   helper(root)

   return max_diameter


def main():
   root = TreeNode(1)
   root.left = TreeNode(2)
   root.right = TreeNode(3)
   root.left.left = TreeNode(4)
   root.right.left = TreeNode(5)
   root.right.right = TreeNode(6)
   print("Tree Diameter: " + str(find_diameter(root)))


   root.left.left = None
   root.right.left.left = TreeNode(7)
   root.right.left.right = TreeNode(8)
   root.right.right.left = TreeNode(9)
   root.right.left.right.left = TreeNode(10)
   root.right.right.left.left = TreeNode(11)
   print("Tree Diameter: " + str(find_diameter(root)))

if __name__ == "__main__":
   main()

