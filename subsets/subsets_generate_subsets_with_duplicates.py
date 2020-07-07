
'''
Problem Statement
Given a set of numbers that might contain duplicates, find all of its distinct subsets.

Example 1:

Input: [1, 3, 3]
Output: [], [1], [3], [1,3], [3,3], [1,3,3]
Example 2:

Input: [1, 5, 3, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3] 
'''

def generate_subsets(nums):
   if len(nums) == 0:
      return []

   subsets = [[]]

   start_index, end_index = 0, 0

   for i in range(len(nums)):
      start_index = 0
      if i > 0 and nums[i-1] == nums[i]:
         start_index = end_index
      
      end_index = len(subsets)

      for j in range(start_index, end_index):
         temp = list(subsets[j])
         temp.append(nums[i])
         subsets.append(temp)
   
   return subsets

def main():
   nums = [1, 3, 3]
   subsets = generate_subsets(nums)
   print(subsets)

   nums = [1, 5, 3, 3]
   subsets = generate_subsets(nums)
   print(subsets)

if __name__ == "__main__":
   main()

