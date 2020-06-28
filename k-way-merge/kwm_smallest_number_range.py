
'''
Problem Statement #
Given ‘M’ sorted arrays, find the smallest range that includes at least one number from each of the ‘M’ lists.

Example 1:

Input: L1=[1, 5, 8], L2=[4, 12], L3=[7, 8, 10]
Output: [4, 7]
Explanation: The range [4, 7] includes 5 from L1, 4 from L2 and 7 from L3.
Example 2:

Input: L1=[1, 9], L2=[4, 12], L3=[7, 10, 16]
Output: [9, 12]
Explanation: The range [9, 12] includes 9 from L1, 12 from L2 and 10 from L3.
'''
from heapq import *
import math

def find_smallest_range(L):
   range_start = -math.inf
   range_end = math.inf

   curr_max = -math.inf # keep track of the current max value of all elements in heap
   M = len(L)
   min_heap = []

   for i in range(M):
      curr_max = max(curr_max, L[i][0])
      heappush(min_heap, (L[i][0], 0, L[i]))

   while min_heap:
      curr_min, index, arr = heappop(min_heap)

      # check if current is less that previous minimum
      if curr_max-curr_min < range_end - range_start:
         range_start = curr_min
         range_end = curr_max
      
      if index+ 1 < len(arr):
         curr_max = max(curr_max, arr[index+1])
         heappush(min_heap, (arr[index+1], index+1, arr))
      
      # this is important to make sure that we are considering all the M sorted list for 
      # computing the smallest range
      if len(min_heap) < M:
         break
   
   return [range_start, range_end]

def main():
   L = [[1, 5, 8], [4, 12], [7, 8, 10]]
   print("Smallest range in '{0}' is {1}".format(L,find_smallest_range(L)))

   L = [[1, 9], [4, 12], [7, 10, 16]]
   print("Smallest range in '{0}' is {1}".format(L,find_smallest_range(L)))

if __name__ == "__main__":
   main()

