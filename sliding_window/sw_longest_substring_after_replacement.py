#!/usr/bin/python

'''
Longest Substring with Same Letters after Replacement

Problem Statement #
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

Example 1:

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
Example 2:

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
Example 3:

Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".

'''

def max_length_substring(str, k):
    char_freq = {}
    max_repeat_leter_count = 0
    ws = 0
    max_len = 0
    for we in range(len(str)):
        rc = str[we]
        char_freq[rc] = char_freq.get(rc,0) + 1
        # at any given point keep track of the max count in the current window
        max_repeat_leter_count = max(max_repeat_leter_count, char_freq[rc])

        #if number of replaceable chrs exceed K shrink the window
        if (we-ws+1) - max_repeat_leter_count > k:
            lc = str[ws]
            ws += 1
            char_freq[lc] -= 1
        
        max_len = max(max_len, we-ws+1)

    return max_len

def main():
    k = 2
    str = "aabccbb"
    print("Max length of substring of '{0}' after replacement is {1}".format(str,max_length_substring(str,k)))

    k = 1
    str = "abbcb"
    print("Max length of substring of '{0}' after replacement is {1}".format(str,max_length_substring(str,k)))

    k = 1
    str = "abccde"
    print("Max length of substring of '{0}' after replacement is {1}".format(str,max_length_substring(str,k)))


if __name__ == "__main__":
    main()