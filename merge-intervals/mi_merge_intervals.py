
'''
Problem Statement #
Given a list of intervals, merge all the overlapping intervals to produce 
a list that has only mutually exclusive intervals.

Example 1:

Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into 
one [1,5].

Example 2:

Intervals: [[6,7], [2,4], [5,9]]
Output: [[2,4], [5,9]]
Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].
 
Example 3:

Intervals: [[1,4], [2,6], [3,5]]
Output: [[1,6]]
Explanation: Since all the given intervals overlap, we merged them into one.
'''

def merge_intervals(intervals):

   if len(intervals) == 0:
      return []
   intervals.sort(key=lambda x: x[0])

   start = intervals[0][0]
   end = intervals[0][1]
   result = []
   for i in range(1,len(intervals)):
      if intervals[i][0] <= end:
         end = max(end, intervals[i][1])
      else:
         result.append([start,end])

         start = intervals[i][0]
         end = intervals[i][1]
   
   result.append([start,end])

   return result

def main():
   # intervals = [[6,7], [2,4], [5,9]]
   intervals = [[1,4], [2,5], [7,9]]
   merged = merge_intervals(intervals)
   print("Merged intervals for {0} are {1}".format(intervals, merged))

   intervals = [[6,7], [2,4], [5,9]]
   merged = merge_intervals(intervals)
   print("Merged intervals for {0} are {1}".format(intervals, merged))

   intervals = [[1,4], [2,6], [3,5]]
   merged = merge_intervals(intervals)
   print("Merged intervals for {0} are {1}".format(intervals, merged))

if __name__ == "__main__":
   main()

