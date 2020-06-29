
'''
Search in Rotated Array
Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number, find if a given ‘key’ is present in it.

Write a function to return the index of the ‘key’ in the rotated array. If the ‘key’ is not present, return -1. You can assume that the given array does not have any duplicates.

Example 1:

Input: [10, 15, 1, 3, 8], key = 15
Output: 1
Explanation: '15' is present in the array at index '1'.

Example 2:

Input: [4, 5, 7, 9, 10, -1, 2], key = 10
Output: 4
Explanation: '10' is present in the array at index '4'.
'''

def bsearch_rotated_array(nums, key):
   start = 0
   end = len(nums) - 1

   while start <= end:
      m = start + (end-start) // 2

      if key == nums[m]:
         return m
      
      if nums[start] <= nums[m]: # determine which side is sorted

         if key >= nums[start] and key < nums[m]: # check if key is within sorted range
            end = m - 1
         else:
            start = m + 1
      else:

         if key <= nums[end] and key > nums[m]: # check if key is wihtin sorted range
            start = m + 1
         else:
            end = m - 1
   
   return -1



def main():
   nums = [10, 15, 1, 3, 8]
   key = 15
   print("Index of {0} in {1} is {2}".format(key, nums,bsearch_rotated_array(nums,key)))

   nums = [4, 5, 7, 9, 10, -1, 2]
   key = 10
   print("Index of {0} in {1} is {2}".format(key, nums,bsearch_rotated_array(nums,key)))

   nums = [10, 15, 1, 3, 8]
   key = 2
   print("Index of {0} in {1} is {2}".format(key, nums,bsearch_rotated_array(nums,key)))

   nums = [10, 15, 1, 3, 8]
   key = 12
   print("Index of {0} in {1} is {2}".format(key, nums,bsearch_rotated_array(nums,key)))

if __name__ == "__main__":
   main()

