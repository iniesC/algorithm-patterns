
'''
Problem Statement #
We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. 
Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

Example 1:

Input: [4, 0, 3, 1]
Output: 2
Example 2:

Input: [8, 3, 5, 2, 4, 6, 0, 1]
Output: 7
'''
def find_missing_number(nums):

   N = len(nums)

   i = 0
   while i < N:
      j = nums[i]
      if j < N and nums[i] != nums[j]:
         nums[i], nums[j] = nums[j], nums[i]
      else:
         i += 1
   
   for i in range(N):
      if i != nums[i]:
         return i

def main():
   nums = [4, 0, 3, 1]
   n = find_missing_number(nums)
   print("Missing number in {0} is {1}".format(nums, n))

   nums = [8, 3, 5, 2, 4, 6, 0, 1]
   n = find_missing_number(nums)
   print("Missing number in {0} is {1}".format(nums, n))


if __name__ == "__main__":
   main()

