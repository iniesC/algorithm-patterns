
'''
Rearrange String K Distance Apart
Given a string and a number ‘K’, find if the string can be rearranged such that the same characters are at least ‘K’ distance apart from each other.

Example 1:

Input: "mmpp", K=2
Output: "mpmp" or "pmpm"
Explanation: All same characters are 2 distance apart.
Example 2:

Input: "Programming", K=3
Output: "rgmPrgmiano" or "gmringmrPoa" or "gmrPagimnor" and a few more
Explanation: All same characters are 3 distance apart.
Example 3:

Input: "aab", K=2
Output: "aba"
Explanation: All same characters are 2 distance apart.
Example 4:

Input: "aappa", K=3
Output: ""
Explanation: We cannot find an arrangement of the string where any two 'a' are 3 distance apart.
'''
from heapq import *

def rearrange_string(str, K):
   char_freq = {}
   for c in str:
      char_freq[c] = char_freq.get(c,0) + 1
   
   max_heap = []
   for c, f in char_freq.items():
      heappush(max_heap, (-f,c))
   
   resultStr = ""
   q = []

   while max_heap:
      f, c = heappop(max_heap)

      resultStr += c
      q.append((f+1,c))

      if len(q) >=  K:
         f,c = q.pop(0)

         if f != 0:
            heappush(max_heap, (f,c))

   return resultStr if len(resultStr) == len(str) else ""




def main():
   str = "mmpp"
   K=2
   print(rearrange_string(str, K))

   str = "Programming"
   K=3
   print(rearrange_string(str, K))

   str = "aab"
   K=2
   print(rearrange_string(str, K))

   str = "aappa"
   K=3
   print(rearrange_string(str, K))

if __name__ == "__main__":
   main()

