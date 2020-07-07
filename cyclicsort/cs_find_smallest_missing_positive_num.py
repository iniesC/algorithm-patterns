
'''
Find the Smallest Missing Positive Number (medium) #
Given an unsorted array containing numbers, find the smallest missing positive number in it.

Example 1:

Input: [-3, 1, 5, 4, 2]
Output: 3
Explanation: The smallest missing positive number is '3'
Example 2:

Input: [3, -2, 0, 1, 2]
Output: 4
Example 3:

Input: [3, 2, 5, 1]
Output: 4
'''

def find_smallest_missing(nums):
   N = len(nums)

   i = 0
   while i < N:
      j = nums[i] -1

      if j >= 0 and j < N and nums[i] != nums[j]:
         nums[i], nums[j] = nums[j], nums[i]
      else:
         i += 1
   
   for i in range(N):
      if i+1 != nums[i]:
         return i+1


def main():
   nums = [-3, 1, 5, 4, 2]
   n = find_smallest_missing(nums)
   print("Smallest missing positive in {0} is {1}".format(nums,n))

   nums = [3, -2, 0, 1, 2]
   n = find_smallest_missing(nums)
   print("Smallest missing positive in {0} is {1}".format(nums,n))

   nums = [-3, -2, -5, -1]
   n = find_smallest_missing(nums)
   print("Smallest missing positive in {0} is {1}".format(nums,n))

if __name__ == "__main__":
   main()

