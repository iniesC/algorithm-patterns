
'''
Problem Statement #
We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. 
The array has some duplicates, find all the duplicate numbers without using any extra space.

Example 1:

Input: [3, 4, 4, 5, 5]
Output: [4, 5]
Example 2:

Input: [5, 4, 7, 2, 3, 5, 3]
Output: [3, 5]
'''

def find_all_duplicates(nums):
   N = len(nums)

   i = 0
   while i < N:
      j = nums[i] - 1

      if nums[i] != nums[j]:
         nums[i], nums[j] = nums[j], nums[i]
      else:
         i += 1
   
   result = []
   for i in range(N):
      if i+1 != nums[i]:
         result.append(nums[i])
   
   return result

def main():
   nums = [3, 4, 4, 5, 5]
   dups = find_all_duplicates(nums)
   print("All duplicates in {0} are {1}".format(nums, dups))


if __name__ == "__main__":
   main()

