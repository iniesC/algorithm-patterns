
'''
Problem Statement
Given an array with positive numbers and a target number, find all of its contiguous subarrays whose product is less than the target number.

Example 1:

Input: [2, 5, 3, 10], target=30 
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarrays whose product is less than the target.
Example 2:

Input: [8, 2, 6, 5], target=50 
Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] 
Explanation: There are seven contiguous subarrays whose product is less than the target.
'''
from collections import deque

def find_subarray(nums, target):
   result = []
   ws = 0
   prod = 1

   for we in range(len(nums)):

      prod *= nums[we]

      while prod >= target and ws < len(nums):
         prod /= nums[ws]
         ws += 1
      
      temp = deque()
      for i in range(we, ws-1, -1):
         temp.appendleft(nums[i])
         result.append(list(temp))
   
   return result


def main():
   nums = [2, 5, 3, 10] 
   target=30
   result = find_subarray(nums, target)
   print(result)

   nums = [8, 2, 6, 5]
   target=50
   result = find_subarray(nums, target)
   print(result)

if __name__ == "__main__":
   main()

