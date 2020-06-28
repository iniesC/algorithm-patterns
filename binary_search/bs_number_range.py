
'''
Find number range in a given array

Problem Statement #
Given an array of numbers sorted in ascending order, find the range of a given number ‘key’. The range of the ‘key’ will be the first and last position of the ‘key’ in the array.

Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].

Example 1:

Input: [4, 6, 6, 6, 9], key = 6
Output: [1, 3]
Example 2:

Input: [1, 3, 8, 10, 15], key = 10
Output: [3, 3]
Example 3:

Input: [1, 3, 8, 10, 15], key = 12
Output: [-1, -1]
'''

def bsearch(arr, key, flag= True):
   start = 0
   end = len(arr) - 1
   keyindex = -1

   while start <= end:
      m = start + (end - start) // 2

      if key < arr[m]:
         end = m - 1
      elif key > arr[m]:
         start = m + 1
      else:
         keyindex = m

         if flag:
            start = m + 1
         else:
            end = m - 1
   
   return keyindex

def find_number_range(arr, key):
   lower = -1
   higher = -1
   lower = bsearch(arr, key, False)
   if lower != -1:
      higher = bsearch(arr, key, True)
   
   return [lower, higher]

def main():
   arr = [4, 6, 6, 6, 9]
   key = 6
   print("Index range for {0} in {1} is {2}".format(key, arr,find_number_range(arr, key)))

   arr = [1, 3, 8, 10, 15]
   key = 10
   print("Index range for {0} in {1} is {2}".format(key, arr,find_number_range(arr, key)))

   arr = [1, 3, 8, 10, 15]
   key = 12
   print("Index range for {0} in {1} is {2}".format(key, arr,find_number_range(arr, key)))

if __name__ == "__main__":
   main()

