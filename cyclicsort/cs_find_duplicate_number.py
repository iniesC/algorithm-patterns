
'''
Problem Statement 
We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. 
The array has only one duplicate but it can be repeated multiple times. 
Find that duplicate number without using any extra space. 
You are, however, allowed to modify the input array.

Example 1:

Input: [1, 4, 4, 3, 2]
Output: 4
Example 2:

Input: [2, 1, 3, 3, 5, 4]
Output: 3
Example 3:

Input: [2, 4, 1, 4, 4]
Output: 4
'''

def find_duplicate_number(nums):
   N = len(nums)

   i = 0
   while i < N:
      j = nums[i] - 1

      if i != j: 
         if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
         else:
            return nums[i]
      else:
         i += 1
   
   return -1

def main():
   nums = [1, 4, 4, 3, 2]
   n = find_duplicate_number(nums)
   print("Duplicate number in {0} is {1}".format(nums, n))


if __name__ == "__main__":
   main()

