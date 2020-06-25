#!/usr/bin/python

'''
Longest Substring with K distinct characters

Problem Statement #
Given a string, find the length of the longest substring in it with no more 
than K distinct characters.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters 
is "araa".
Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters 
is "aa".
Example 3:

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters 
are "cbbeb" & "bbebi".
'''

def length_longest_substring(str, k):
    if k <= 0 or not str:
        return str
    
    char_freq = {}
    ws = 0
    max_len = 0

    for we in range(len(str)):
        rc = str[we]
        char_freq[rc] = char_freq.get(rc,0) + 1

        while len(char_freq) > k: # if the number of distinct chars increases more than K shrink the window
            lc = str[ws]
            ws += 1
            char_freq[lc] -= 1
            if char_freq[lc] == 0:
                del char_freq[lc]

        if we-ws+1 > max_len:
            max_len = we-ws+1
    
    return max_len


def main():

    #Test 1
    k = 2
    str = "araaci"
    print("Length of Longest string in '{0}' is {1}".format(str, length_longest_substring(str,k)))

    #Test 2
    k = 1
    str = "araaci"
    print("Length of Longest string in '{0}' is {1}".format(str, length_longest_substring(str,k)))

    #Test 3
    k = 3
    str = "cbbebi"
    print("Length of Longest string in '{0}' is {1}".format(str, length_longest_substring(str,k)))



if __name__ == "__main__":
    main()
