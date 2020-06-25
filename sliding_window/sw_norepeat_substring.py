#!/usr/bin/python

'''
No-repeat substring

Problem Statement #
Given a string, find the length of the longest substring which has no repeating characters.

Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".
Example 3:

Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".

'''

def max_length_norepeat_substring(str):
    char_index = {} # store the index or position of when the characters are seen in the str
    ws = 0
    max_len = 0

    for we in range(len(str)):
        rc = str[we]
        if rc in char_index:
            ws = max(ws, char_index[rc]+1) #move the starting pointer to the new position
        char_index[rc] = we
        
        max_len = max(max_len, we-ws+1)
    
    return max_len

def main():
    str = "aabccbb"
    print("Max length of non repeat string in '{0}' is {1}".format(str,max_length_norepeat_substring(str)))

    str = "abbbb"
    print("Max length of non repeat string in '{0}' is {1}".format(str,max_length_norepeat_substring(str)))

    str = "abccde"
    print("Max length of non repeat string in '{0}' is {1}".format(str,max_length_norepeat_substring(str)))

if __name__ == "__main__":
    main()
