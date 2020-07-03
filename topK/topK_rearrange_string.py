
'''
Problem Statement
Given a string, find if its letters can be rearranged in such a way that no two same characters come next to each other.

Example 1:

Input: "aappp"
Output: "papap"
Explanation: In "papap", none of the repeating characters come next to each other.
Example 2:

Input: "Programming"
Output: "rgmrgmPiano" or "gmringmrPoa" or "gmrPagimnor", etc.
Explanation: None of the repeating characters come next to each other.
Example 3:

Input: "aapa"
Output: ""
Explanation: In all arrangements of "aapa", atleast two 'a' will come together e.g., "apaa", "paaa".
'''
from heapq import *
def rearrange_string(str):

   char_freq = {}
   for c in str:
      char_freq[c] = char_freq.get(c,0) + 1
   
   max_heap = []
   for c,f in char_freq.items():
      heappush(max_heap, (-f, c))
   
   q = []
   resultStr = ""
   while max_heap:
      f, c = heappop(max_heap)

      resultStr += c
      q.append((f+1,c))

      if len(q) > 1:
         f,c = q.pop(0)
         if f != 0:
            heappush(max_heap, (f,c))

   return resultStr if len(resultStr) == len(str) else ""


def main():
   str = "aappp"
   print(rearrange_string(str))

   str = "Programming"
   print(rearrange_string(str))

   str = "aapa"
   print(rearrange_string(str))

if __name__ == "__main__":
   main()

