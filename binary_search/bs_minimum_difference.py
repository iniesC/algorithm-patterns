
'''
Find the minimum difference number

Problem Statement #
Given an array of numbers sorted in ascending order, find the element in the array that has the minimum difference with the given ‘key’.

Example 1:

Input: [4, 6, 10], key = 7
Output: 6
Explanation: The difference between the key '7' and '6' is minimum than any other number in the array 
Example 2:

Input: [4, 6, 10], key = 4
Output: 4
Example 3:

Input: [1, 3, 8, 10, 15], key = 12
Output: 10
Example 4:

Input: [4, 6, 10], key = 17
Output: 10
'''

def find_min_difference(nums, key):
   start = 0
   end = len(nums) - 1

   if key <= nums[start]:
      return nums[start]
   if key >= nums[end]:
      return nums[end]


   while start <= end:
      m = start + (end-start) // 2

      if key == nums[m]:
         return nums[m]
      
      if key < nums[m]:
         end = m - 1
      else:
         start = m + 1
   
   if abs(nums[start]-key) < abs(nums[end]-key):
      return nums[start]
   else:
      return nums[end]


def main():
   nums = [4, 6, 10] 
   key = 7
   print("Element closer to {0} in {1} is {2}".format(key, nums,find_min_difference(nums, key)))

   nums = [4, 6, 10] 
   key = 4
   print("Element closer to {0} in {1} is {2}".format(key, nums,find_min_difference(nums, key)))

   nums = [1, 3, 8, 10, 15]
   key = 12
   print("Element closer to {0} in {1} is {2}".format(key, nums,find_min_difference(nums, key)))

   nums = [4, 6, 10] 
   key = 17
   print("Element closer to {0} in {1} is {2}".format(key, nums,find_min_difference(nums, key)))

if __name__ == "__main__":
   main()

