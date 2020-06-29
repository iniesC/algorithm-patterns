
'''
Rotation Count (medium) #
Given an array of numbers which is sorted in ascending order and is rotated ‘k’ times around a pivot, find ‘k’.

You can assume that the array does not have any duplicates.

Example 1:

Input: [10, 15, 1, 3, 8]
Output: 2
Explanation: The array has been rotated 2 times.
  
Example 2:

Input: [4, 5, 7, 9, 10, -1, 2]
Output: 5
Explanation: The array has been rotated 5 times.

Example 3:

Input: [1, 3, 8, 10]
Output: 0
Explanation: The array has been not been rotated.
'''

def bsearch_rotation_count(nums):
   start = 0
   end = len(nums) - 1

   if nums[start] <= nums[end]:
      return 0
   
   while start < end:
      m = start + (end-start) // 2

      if m < end and nums[m] > nums[m+1]:
         return m+1
      if m > start and nums[m-1] > nums[m]:
         return m
      
      if nums[start] <= nums[m]: # left side sorted then search right side
         start = m + 1
      else:
         end = m - 1 # right side sorted search left side

   return 0

def main():
   nums = [10, 15, 1, 3, 8]
   print("Rotation count for {0} is {1}".format(nums,bsearch_rotation_count(nums)))

   nums = [1, 3, 8, 10]
   print("Rotation count for {0} is {1}".format(nums,bsearch_rotation_count(nums)))

   nums = [4, 5, 7, 9, 10, -1, 2]
   print("Rotation count for {0} is {1}".format(nums,bsearch_rotation_count(nums)))

if __name__ == "__main__":
   main()

