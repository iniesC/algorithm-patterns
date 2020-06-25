#!/usr/bin/python

'''
Find a permutation in a  string

Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters it will have n!n! permutations.

Example 1:

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.
Example 2:

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.
Example 3:

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.
Example 4:

Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
'''

def check_permutation_present(str, pattern):
    if not pattern or not str:
        return False

    char_freq = {}
    for c in pattern:
        char_freq[c] = char_freq.get(c,0) + 1
    
    ws = 0
    found = 0

    for we in range(len(str)):
        rc = str[we]

        if rc in char_freq:
            char_freq[rc] -=1
            if char_freq[rc] == 0:
                found += 1
        
        # if all characters freq is found then we found the pattern
        if found == len(char_freq):
            return True
        
        # if we didnt find match with window size equal or greater than pattern size - SHRINK !!
        if we >= len(pattern) - 1:
            lc = str[ws]
            ws += 1
            if lc in char_freq:
                if char_freq[lc] == 0:
                    found -= 1
                char_freq[lc] += 1


    return False


def main():
    str = "oidbcaf"
    pattern = "abc"
    print("Permutation '{0}' is found in '{1}' : {2}".format(pattern, str,check_permutation_present(str, pattern)))

    str = "odicf"
    pattern = "dc"
    print("Permutation '{0}' is found in '{1}' : {2}".format(pattern, str,check_permutation_present(str, pattern)))

    str = "bcdxabcdy"
    pattern = "bcdyabcdx"
    print("Permutation '{0}' is found in '{1}' : {2}".format(pattern, str,check_permutation_present(str, pattern)))

    str = "aaacb"
    pattern = "abc"
    print("Permutation '{0}' is found in '{1}' : {2}".format(pattern, str,check_permutation_present(str, pattern)))

if __name__ == "__main__":
    main()
