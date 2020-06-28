
'''

Problem Statement #
Search Bitonic Array
Given a Bitonic array, find if a given ‘key’ is present in it. An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].

Write a function to return the index of the ‘key’. If the ‘key’ is not present, return -1.

Example 1:
Input: [1, 3, 8, 4, 3], key=4
Output: 3

Example 2:
Input: [3, 8, 3, 1], key=8
Output: 1

Example 3:
Input: [1, 3, 8, 12], key=12
Output: 3

Example 4:
Input: [10, 9, 8], key=10
Output: 0
'''

# Fidn the peak on a bitonic array is key to solve this problem
def find_peak(nums):
   start = 0
   end = len(nums) - 1

   while start < end:
      m = start + (end-start) // 2

      if nums[m] < nums[m+1]:
         start = m + 1
      else:
         end = m
   
   return start

# Regular binary search looking for key in an sorted array
# Order of sort is unknown and returns index is found else -1
def bsearch(nums, key, start, end):
   isAsc = True
   if nums[start] >= nums[end]:
      isAsc = False
   
   while start <= end:
      m = start + (end-start) //2

      if key == nums[m]:
         return m
      
      if isAsc:
         if key < nums[m]:
            end = m - 1
         else:
            start = m + 1
      else:
         if key < nums[m]:
            start = m + 1
         else:
            end = m - 1
   
   return -1

def search_bitonic(nums, key):
   if not nums:
      return -1
   
   # Find the peak index
   peak_index = find_peak(nums)
   start = 0
   end = len(nums) - 1

   #search first half
   first_search = bsearch(nums,key,start, peak_index)
   if first_search != -1:
      return first_search
   
   # Search second half if needed
   second_search = bsearch(nums, key, peak_index+1, end)

   return second_search

def main():
   nums = [1, 3, 8, 4, 3]
   key = 4
   print("Index for {0} in array {1} is {2}".format(key, nums,search_bitonic(nums, key)))

   nums = [3, 8, 3, 1]
   key = 8
   print("Index for {0} in array {1} is {2}".format(key, nums,search_bitonic(nums, key)))

   nums = [1, 3, 8, 12, 4, 2]
   key = 12
   print("Index for {0} in array {1} is {2}".format(key, nums,search_bitonic(nums, key)))

   nums = [10, 9, 8]
   key = 10
   print("Index for {0} in array {1} is {2}".format(key, nums,search_bitonic(nums, key)))


   nums = [1, 3, 8, 12, 4, 2]
   key = 15
   print("Index for {0} in array {1} is {2}".format(key, nums,search_bitonic(nums, key)))

if __name__ == "__main__":
   main()

