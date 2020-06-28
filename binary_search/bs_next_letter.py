
'''
Problem Statement #
Given an array of lowercase letters sorted in ascending order, find the smallest letter in the given array greater than a given ‘key’.

Assume the given array is a circular list, which means that the last letter is assumed to be connected with the first letter. This also means that the smallest letter in the given array is greater than the last letter of the array and is also the first letter of the array.

Write a function to return the next letter of the given ‘key’.

Example 1:

Input: ['a', 'c', 'f', 'h'], key = 'f'
Output: 'h'
Explanation: The smallest letter greater than 'f' is 'h' in the given array.
Example 2:

Input: ['a', 'c', 'f', 'h'], key = 'b'
Output: 'c'
Explanation: The smallest letter greater than 'b' is 'c'.
Example 3:

Input: ['a', 'c', 'f', 'h'], key = 'm'
Output: 'a'
Explanation: As the array is assumed to be circular, the smallest letter greater than 'm' is 'a'.
Example 4:

Input: ['a', 'c', 'f', 'h'], key = 'h'
Output: 'a'
Explanation: As the array is assumed to be circular, the smallest letter greater than 'h' is 'a'.
'''

def next_letter(arr, key):
   start = 0
   end = len(arr) - 1

   while start <= end:
      m = start + (end-start) // 2

      if key < arr[m]:
         end = m-1
      else:
         start = m+1

   return arr[start] if start < len(arr) else arr[0]

def main():
   arr = ['a', 'c', 'f', 'h']
   key = 'f'
   print("Next letter of '{0}' in {1} is '{2}'".format(key, arr, next_letter(arr, key)))

   arr = ['a', 'c', 'f', 'h']
   key = 'b'
   print("Next letter of '{0}' in {1} is '{2}'".format(key, arr, next_letter(arr, key)))

   arr = ['a', 'c', 'f', 'h']
   key = 'm'
   print("Next letter of '{0}' in {1} is '{2}'".format(key, arr, next_letter(arr, key)))

   arr = ['a', 'c', 'f', 'h']
   key = 'h'
   print("Next letter of '{0}' in {1} is '{2}'".format(key, arr, next_letter(arr, key)))


if __name__ == "__main__":
   main()

