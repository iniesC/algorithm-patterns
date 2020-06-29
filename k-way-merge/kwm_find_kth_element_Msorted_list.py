
'''
Problem Statement
Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

Example 1:

Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
Output: 4
Explanation: The 5th smallest number among all the arrays is 4, this can be verified from the merged 
list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]
Example 2:

Input: L1=[5, 8, 9], L2=[1, 7], K=3
Output: 7
Explanation: The 3rd smallest number among all the arrays is 7.
'''

from heapq import *

def find_Kth_element(L, K):
   if not L or K == 0:
      return -1

   M = len(L)

   min_heap = []
   cnt = 0

   for i in range(M):
      heappush(min_heap, (L[i][0], 0, L[i]))
   
   while min_heap:
      num, index, arr = heappop(min_heap)

      cnt += 1

      if cnt == K:
         return num
      
      if index + 1 < len(arr):
         heappush(min_heap, (arr[index+1], index+1, arr))

   return -1

def main():
   L = [[2, 6, 8], [3, 6, 7], [1, 3, 4]]
   K = 5
   print(find_Kth_element(L,K))

   L = [[5, 8, 9], [1, 7]]
   K = 3
   print(find_Kth_element(L,K))


if __name__ == "__main__":
   main()

