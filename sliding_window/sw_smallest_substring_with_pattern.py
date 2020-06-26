
'''
Smallest Substring containing the pattern
Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

Example 1:

Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"
Example 2:

Input: String="abdabca", Pattern="abc"
Output: "abc"
Explanation: The smallest substring having all characters of the pattern is "abc".
Example 3:

Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.
'''
import math
def get_smallest_substring(str, pattern):
   if not pattern or not str:
      return ""
   
   char_freq = {}
   for c in pattern:
      char_freq[c] = char_freq.get(c,0) + 1
   
   ws = 0
   min_len = math.inf
   start_index = 0
   found = 0

   for we in range(len(str)): # learning: we values are only 0,1,2,3,4,5 (for str of length 6) it does not take the value 6 on exit
      rc = str[we]
      if rc in char_freq:
         char_freq[rc] -= 1
         if char_freq[rc] == 0:
            found += 1
      
      while found == len(char_freq):
         if we-ws+1 < min_len: # when we still have the pattern in substring compute min length
            min_len = we-ws+1
            start_index = ws

         lc = str[ws]
         ws += 1      # SHRINK!!
         if lc in char_freq:
            if char_freq[lc] == 0:
               found -= 1
            char_freq[lc] += 1
   
   return str[start_index:start_index+min_len] if min_len != math.inf else ""

def main():
   str = "aabdec"
   pattern = "abc"
   print("Smallest substring with pattern '{0}' in string '{1}' is '{2}'"\
      .format(pattern,str,get_smallest_substring(str,pattern)))

   str = "abdabca"
   pattern = "abc"
   print("Smallest substring with pattern '{0}' in string '{1}' is '{2}'"\
      .format(pattern,str,get_smallest_substring(str,pattern)))

   str = "adcad"
   pattern = "abc"
   print("Smallest substring with pattern '{0}' in string '{1}' is '{2}'"\
      .format(pattern,str,get_smallest_substring(str,pattern)))

if __name__ == "__main__":
   main()

