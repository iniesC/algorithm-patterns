
'''
Problem Statement #
Given a set of distinct numbers, find all of its permutations.

Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following six permutations:

{1, 2, 3}
{1, 3, 2}
{2, 1, 3}
{2, 3, 1}
{3, 1, 2}
{3, 2, 1}
If a set has ‘n’ distinct elements it will have n!n! permutations.

Example 1:

Input: [1,3,5]
Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]
'''

def generate_permutations(nums):

   result = []

   def helper(nums, curr_perm, remaining):
      if remaining == 0:
         result.append(list(curr_perm))
         return 
      
      for i in range(len(nums)):
         curr_perm.append(nums[i])
         helper(nums[:i]+nums[i+1:], curr_perm, remaining-1)
         del curr_perm[-1]
   
   helper(nums,[], len(nums))

   return result

def permutation_bfs(nums):
   if len(nums) == 0:
      return []
   
   perm = [[]]
   result = []

   for n in nums:
      length = len(perm)
         
      for _ in range(length):
         oldperm = perm.pop(0)
         
         for j in range(len(oldperm)+1):
            newperm = list(oldperm)
            newperm.insert(j,n)

            if len(newperm) >= len(nums):
               result.append(newperm)
            else:
               perm.append(newperm)

   return result

def main():
   nums = [1,3,5]
   perm = generate_permutations(nums)
   print(perm)

   nums = [1,3,5]
   perm = permutation_bfs(nums)
   print(perm)

   nums = [1,2, 3]
   perm = generate_permutations(nums)
   print(perm)

if __name__ == "__main__":
   main()

