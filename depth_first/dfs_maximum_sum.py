
'''
Path with Maximum Sum 
Find the path with the maximum sum in a given binary tree.
 Write a function that returns the maximum sum. 
 A path can be defined as a sequence of nodes between any two nodes and 
 doesn’t necessarily pass through the root.
'''
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def find_maximumsum(root):
   max_sum= 0

   def helper(root):
      nonlocal max_sum

      if not root:
         return 0
      
      left_height = helper(root.left)
      right_height = helper(root.right)

      diameter = root.val + left_height + right_height

      max_sum = max(max_sum, diameter)

      return root.val + max(left_height, right_height)
   
   helper(root)

   return max_sum


def main():
   root = TreeNode(1)
   root.left = TreeNode(2)
   root.right = TreeNode(3)
   root.left.left = TreeNode(4)
   root.right.left = TreeNode(5)
   root.right.right = TreeNode(6)
   print("Tree Diameter: " + str(find_maximumsum(root)))


   root.left.left = None
   root.right.left.left = TreeNode(7)
   root.right.left.right = TreeNode(8)
   root.right.right.left = TreeNode(9)
   root.right.left.right.left = TreeNode(10)
   root.right.right.left.left = TreeNode(11)
   print("Tree Diameter: " + str(find_maximumsum(root)))

   root = TreeNode(1)
   root.left = TreeNode(2)
   root.right = TreeNode(3)

   print("Maximum Path Sum: " + str(find_maximumsum(root)))
   root.left.left = TreeNode(1)
   root.left.right = TreeNode(3)
   root.right.left = TreeNode(5)
   root.right.right = TreeNode(6)
   root.right.left.left = TreeNode(7)
   root.right.left.right = TreeNode(8)
   root.right.right.left = TreeNode(9)
   print("Maximum Path Sum: " + str(find_maximumsum(root)))

   root = TreeNode(-1)
   root.left = TreeNode(-3)
   print("Maximum Path Sum: " + str(find_maximumsum(root)))

if __name__ == "__main__":
   main()


