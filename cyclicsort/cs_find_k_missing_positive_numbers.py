
'''
Find the First K Missing Positive Numbers
Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array.

Example 1:

Input: [3, -1, 4, 5, 5], k=3
Output: [1, 2, 6]
Explanation: The smallest missing positive numbers are 1, 2 and 6.
Example 2:

Input: [2, 3, 4], k=3
Output: [1, 5, 6]
Explanation: The smallest missing positive numbers are 1, 5 and 6.
Example 3:

Input: [-2, -3, 4], k=2
Output: [1, 2]
Explanation: The smallest missing positive numbers are 1 and 2.
'''

def find_k_missing(nums, k):
   N = len(nums)

   i = 0
   while i < N:
      j = nums[i] - 1

      if j >= 0 and j < N and nums[i] != nums[j]:
         nums[i], nums[j] = nums[j], nums[i]
      
      else:
         i += 1
   
   result = []
   i = 0
   while k > 0 and i < N:
      if i+1 != nums[i]:
         result.append(i+1)
         k -= 1
      i += 1
   
   value = nums[N-1]
   while k > 0:
      value += 1
      result.append(value)
      k -= 1

   return result

def main():
   nums = [3, -1, 4, 5, 5]
   k=3
   miss = find_k_missing(nums,k)
   print("K missing positive numbers in {0} are {1}".format(nums,miss))


   nums = [2, 3, 4]
   k=3
   miss = find_k_missing(nums,k)
   print("K missing positive numbers in {0} are {1}".format(nums,miss))

   nums = [-2, -3, 4]
   k=2
   miss = find_k_missing(nums,k)
   print("K missing positive numbers in {0} are {1}".format(nums,miss))

if __name__ == "__main__":
   main()

