
'''
Problem Statement 
Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

Example 1:

Input: [1, 3, 5, 12, 11, 12, 11], K = 2
Output: [12, 11]
Explanation: Both '11' and '12' apeared twice.
Example 2:

Input: [5, 12, 11, 3, 11], K = 2
Output: [11, 5] or [11, 12] or [11, 3]
Explanation: Only '11' appeared twice, all other numbers appeared once.
'''
from heapq import *

def find_topk_frequent_numbers(nums,K):

   freq = {}
   for n in nums:
      freq[n] = freq.get(n,0) + 1
   
   min_heap = []

   for n, f in freq.items():
      heappush(min_heap, (f, n))

      if len(min_heap) > K:
         heappop(min_heap)
   
   result = []
   while min_heap:
      result.append(heappop(min_heap)[1])
   
   return result

def main():
   nums = [1, 3, 5, 12, 11, 12, 11]
   K = 2
   print(find_topk_frequent_numbers(nums,K))

if __name__ == "__main__":
   main()

