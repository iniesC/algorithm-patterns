
'''
Problem Statement
Given a set with distinct elements, find all of its distinct subsets.

Example 1:

Input: [1, 3]
Output: [], [1], [3], [1,3]
Example 2:

Input: [1, 5, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
'''

def generate_subsets(nums):
   if len(nums) == 0:
      return []

   subsets = [[]]
   for n in nums:

      length = len(subsets)

      for i in range(length):
         temp = list(subsets[i])
         temp.append(n)
         subsets.append(temp)
   
   print(subsets)

   return subsets


def main():
   nums = [1, 3]
   subsets = generate_subsets(nums)

   nums = [1, 5, 3]
   subsets = generate_subsets(nums)

if __name__ == "__main__":
   main()

