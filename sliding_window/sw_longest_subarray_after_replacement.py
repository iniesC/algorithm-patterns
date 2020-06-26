#!/usr/bin/python

'''
Longest subarray after replacement

Problem Statement #
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

Example 1:

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
Example 2:

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
'''

def max_length_subarray(arr, k):
    max_repeat_one_count = 0 # keep track of number os 1s in current window
    ws = 0
    max_len = 0

    for we in range(len(arr)):
        re = arr[we]
        if re == 1:
            max_repeat_one_count += 1
        
        # shrink window if replaceable count goes above k
        if we-ws+1 - max_repeat_one_count > k:
            le = arr[ws]
            ws += 1
            if le == 1:
                max_repeat_one_count -= 1
        
        max_len = max(max_len, we-ws+1)
    
    return max_len

def main():
    k = 2
    arr = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
    print("Max length of subarray with 1s is ", max_length_subarray(arr,k))

    k = 3
    arr = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
    print("Max length of subarray with 1s is ", max_length_subarray(arr,k))

if __name__ == "__main__":
    main()
