
'''
Ceiling of a number

Problem Statement #
Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’. The ceiling of the ‘key’ will be the smallest element in the given array greater than or equal to the ‘key’.

Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1.

Example 1:

Input: [4, 6, 10], key = 6
Output: 1
Explanation: The smallest number greater than or equal to '6' is '6' having index '1'.
Example 2:

Input: [1, 3, 8, 10, 15], key = 12
Output: 4
Explanation: The smallest number greater than or equal to '12' is '15' having index '4'.
Example 3:

Input: [4, 6, 10], key = 17
Output: -1
Explanation: There is no number greater than or equal to '17' in the given array.
Example 4:

Input: [4, 6, 10], key = -1
Output: 0
Explanation: The smallest number greater than or equal to '-1' is '4' having index '0'.
'''

def find_ceiling_index(arr, key):
   start = 0
   end = len(arr) - 1

   while start <= end:
      m = start + (end-start) // 2

      if arr[m] == key:
         return m
      
      if key < arr[m]:
         end = m -1
      else:
         start = m + 1
   

   return start if start < len(arr) else -1


def main():
   arr = [4, 6, 10]
   key = 6
   print("Ceiling for {0} in {1} is {2}".format(key, arr,find_ceiling_index(arr, key)))

   arr = [1, 3, 8, 10, 15]
   key = 12
   print("Ceiling for {0} in {1} is {2}".format(key, arr,find_ceiling_index(arr, key)))

   arr = [4, 6, 10]
   key = 17
   print("Ceiling for {0} in {1} is {2}".format(key, arr,find_ceiling_index(arr, key)))

   arr = [4, 6, 10]
   key = -1
   print("Ceiling for {0} in {1} is {2}".format(key, arr,find_ceiling_index(arr, key)))

if __name__ == "__main__":
   main()

