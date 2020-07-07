
'''
Problem Statement 
Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

Example 1:

Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: The output list contains the common intervals between the two lists.
Example 2:

Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
Output: [5, 7], [9, 10]
Explanation: The output list contains the common intervals between the two lists.
'''

def find_interval_intersect(A,B):
   N1 = len(A)
   N2 = len(B)

   start = 0
   end = 1

   i , j = 0,0
   intersect = []
   while i < N1 and j < N2:
      a = A[i]
      b = B[j]

      aonb = (b[start] >= a[start] and b[start] <= a[end])
      bona = (b[end] >= a[start] and b[end] <= a[end])

      if aonb or bona:
           istart = max(a[start], b[start])
           iend = min(a[end], b[end])
           intersect.append([istart, iend])
      
      if a[end] < b[end]:
         i += 1
      else:
         j += 1

   print(intersect)

   return intersect 


def main():
   arr1=[[1, 3], [5, 6], [7, 9]]
   arr2=[[2, 3], [5, 7]]
   intersect = find_interval_intersect(arr1, arr2)

if __name__ == "__main__":
   main()

