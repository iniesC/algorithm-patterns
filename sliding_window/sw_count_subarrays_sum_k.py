
'''
Problem Statement: Given an array of integers count the number of subarrays with sum equal to K.

Example 1:
arr = [1,1,1] and k = 2
output = 2
Explanation: [1,1] and [1,1] 2 sub arrays add up to K = 2
'''

# Solution is O(N^3) time complexity and O(1) space
def count_subarrays_NcubeSolution(arr, k):
   N = len(arr)
   cnt = 0
   for start in range(N):
      for end in range(start+1, N+1):
         sum = 0
         for i in range(start, end):
            sum += arr[i]
         if sum == k:
            cnt +=1
   
   return cnt

# Solution is O(N^2) time complexity and O(N) space
def count_subarrays_NsquareSolution(arr,k):
   N = len(arr)
   cnt = 0
   cummulative_sum = [0] * (N+1)
   cummulative_sum[0] = 0
   for i in range(1,N+1):
      cummulative_sum[i] = cummulative_sum[i-1] + arr[i-1]
   
   for start in range(N):
      for end in range(start+1, N+1):
         sum = cummulative_sum[end] - cummulative_sum[start]
         if sum == k:
            cnt += 1
   
   return cnt 

# Solution is O(N) in time and O(N) in sapce
def count_subarrays_LinearSolution(arr, k):
   cummulative_sum = {}
   N = len(arr)

   sum = 0
   cummulative_sum[sum] = cummulative_sum.get(sum, 0) + 1
   cnt = 0
   for n in arr:
      sum += n
      if sum-k in cummulative_sum:
         cnt += cummulative_sum[sum-k]
      
      cummulative_sum[sum] = cummulative_sum.get(sum,0) + 1
   
   return cnt


# def count_subarrays_slidingwindow(arr, k):
#    ws = 0
#    sum = 0
#    cnt = 0

#    for we in range(len(arr)):
#       sum += arr[we]

#       while sum > k:
#          sum -= arr[ws]
#          ws += 1
      
#       if sum == k:
#          cnt +=1
   
#    return cnt if k!= 0 else 0


def main():
   arr = [1,1,1]
   k = 2
   
   print(count_subarrays_NcubeSolution(arr,k))
   print(count_subarrays_NsquareSolution(arr,k))
   print(count_subarrays_LinearSolution(arr,k))
   # print(count_subarrays_slidingwindow(arr, k))


if __name__ == "__main__":
   main()

