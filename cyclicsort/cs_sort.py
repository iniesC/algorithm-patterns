
'''
Problem Statement
We are given an array containing ‘n’ objects. Each object, when created, was assigned a unique number from 1 to ‘n’ based on their creation sequence. This means that the object with sequence number ‘3’ was created just before the object with sequence number ‘4’.

Write a function to sort the objects in-place on their creation sequence number in O(n)O(n) and without any extra space. For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.

Example 1:

Input: [3, 1, 5, 4, 2]
Output: [1, 2, 3, 4, 5]
Example 2:

Input: [2, 6, 4, 3, 1, 5]
Output: [1, 2, 3, 4, 5, 6]
Example 3:

Input: [1, 5, 6, 4, 3, 2]
Output: [1, 2, 3, 4, 5, 6]
'''

def cyclic_sort(nums):
   N = len(nums)

   i = 0
   while i < N:
      j = nums[i] - 1
      if nums[i] != nums[j]:
         nums[i], nums[j] = nums[j], nums[i]
      else:
         i += 1
   

def main():
   nums = [3, 1, 5, 4, 2]
   cyclic_sort(nums)
   print("Sorted array: ", nums)

   nums = [2, 6, 4, 3, 1, 5]
   cyclic_sort(nums)
   print("Sorted array: ", nums)

   nums = [1, 5, 6, 4, 3, 2]
   cyclic_sort(nums)
   print("Sorted array: ", nums)
if __name__ == "__main__":
   main()

