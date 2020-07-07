
'''
Problem Statement #
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.
Example 2:

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.
'''
def search_pair(nums, low, target, triplets):
   high = len(nums) - 1

   while low < high:
      curr_sum = nums[low] + nums[high]

      if curr_sum == target:
         triplets.append([-target, nums[low], nums[high]])
         low += 1
         high -= 1

         while low < high and nums[low] == nums[low-1]:
            low += 1
         while low < high  and nums[high] == nums[high+1]:
            high -= 1
      elif curr_sum < target:
         low +=1 
      else:
         high -= 1

def find_triplets(nums):
   nums.sort()
   triplets = []
   for i in range(len(nums)-2):
      if i> 0 and nums[i] == nums[i-1]:
         continue
      search_pair(nums, i+1, -nums[i], triplets)
   
   return triplets



def main():
   nums = [-3, 0, 1, 2, -1, 1, -2]
   result = find_triplets(nums)
   print(result)

   nums = [-5, 2, -1, -2, 3]
   result = find_triplets(nums)
   print(result)


if __name__ == "__main__":
   main()

