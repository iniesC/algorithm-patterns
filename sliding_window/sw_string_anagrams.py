
'''
String Anagrams:

Given a string and a pattern, find all anagrams of the pattern in the given string.

Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:

abc
acb
bac
bca
cab
cba
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Example 1:

Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
Example 2:

Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
'''

def getAnagramsStartingIndex(str, pattern):
   char_freq = {}
   for c in pattern:
      char_freq[c] = char_freq.get(c,0) + 1
   
   ws = 0
   result = []
   found = 0

   for we in range(len(str)):
      rc = str[we]
      if rc in char_freq:
         char_freq[rc] -= 1
         if char_freq[rc] == 0:
            found += 1
      
      if found == len(char_freq):
         result.append(ws)
      
      if we >= len(pattern)-1:
         lc = str[ws]
         ws += 1
         if lc in char_freq:
            if char_freq[lc] == 0:
               found -= 1
            char_freq[lc] += 1
   
   return result if result else [-1]

def main():
   str = "ppqp"
   pattern = "pq"
   print("Pattern '{0}' is seen in '{1}' at starting indices is {2}".format(pattern, str, getAnagramsStartingIndex(str, pattern)))

   str = "abbcabc"
   pattern = "abc"
   print("Pattern '{0}' is seen in '{1}' at starting indices is {2}".format(pattern, str, getAnagramsStartingIndex(str, pattern)))


if __name__ == "__main__":
   main()

