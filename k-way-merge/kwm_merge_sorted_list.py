
'''
Problem Statement
Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.

Example 1:

Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]
Example 2:

Input: L1=[5, 8, 9], L2=[1, 7]
Output: [1, 5, 7, 8, 9]
'''
from heapq import *

def merge_sorted_list(L):
   K = len(L)
   result = []

   min_heap = []
   for i in range(K):
      heappush(min_heap, (L[i][0], 0, L[i]))
   
   while min_heap:
      num, index, arr = heappop(min_heap)

      result.append(num)
      if index + 1 < len(arr):
         heappush(min_heap, (arr[index+1], index+1, arr))
   
   return result

def main():
   L = [[2, 6, 8],[3, 6, 7], [1, 3, 4]]
   print(merge_sorted_list(L))

   L = [[5, 8, 9], [1, 7]]
   print(merge_sorted_list(L))

if __name__ == "__main__":
   main()

