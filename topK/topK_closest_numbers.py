
'''
Problem Statement #
Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers to ‘X’ in the array. Return the numbers in the sorted order. ‘X’ is not necessarily present in the array.

Example 1:

Input: [5, 6, 7, 8, 9], K = 3, X = 7
Output: [6, 7, 8]
Example 2:

Input: [2, 4, 5, 6, 9], K = 3, X = 6
Output: [4, 5, 6]
Example 3:

Input: [2, 4, 5, 6, 9], K = 3, X = 10
Output: [5, 6, 9]
'''
from heapq import *

def bsearch(nums, X):
   start = 0
   end = len(nums) - 1

   while start <= end:
      m = start + (end-start) // 2

      if X == nums[m]:
         return m
      
      if X < nums[m]:
         end = m - 1
      else:
         start = m + 1

   if start < len(nums) and abs(nums[start] - X) < abs(nums[end]-X):
      return start
   else:
      return end

def find_closest_numbers(nums, K, X):
   index = bsearch(nums, X)

   start = max(0, index-K)
   end = min(len(nums)-1, index+K)

   min_heap = []
   for i in range(start, end+1):
      heappush(min_heap, (abs(nums[i]-X), nums[i]))
   
   result = []
   for i in range(K):
      result.append(heappop(min_heap)[1])
   
   result.sort()
   return result

def main():
   nums = [5, 6, 7, 8, 9]
   K = 3 
   X = 7
   print(find_closest_numbers(nums, K, X))

   nums = [2, 4, 5, 6, 9]
   K = 3 
   X = 6
   print(find_closest_numbers(nums, K, X))

   nums = [2, 4, 5, 6, 9]
   K = 3 
   X = 10
   print(find_closest_numbers(nums, K, X))

if __name__ == "__main__":
   main()

