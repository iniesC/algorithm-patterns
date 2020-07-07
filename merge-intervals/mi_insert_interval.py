
'''
Problem Statement 
Given a list of non-overlapping intervals sorted by their start time, 
insert a given interval at the correct position and merge all necessary 
intervals to produce a list that has only mutually exclusive intervals.

Example 1:

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].
Example 2:

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
Output: [[1,3], [4,12]]
Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].
Example 3:

Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
Output: [[1,4], [5,7]]
Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].
'''

def insert_interval(intervals, new_interval):
   N = len(intervals)
   # intervals.sort(key=lambda x: x[0])

   start = new_interval[0]
   end = new_interval[1]

   i = 0
   merged = []
   while i < N and start >= intervals[i][1]:
      merged.append([intervals[i][0], intervals[i][1]])
      i += 1

   while i < N and end >= intervals[i][0]:
      start = min(intervals[i][0], start)
      end = max (intervals[i][1], end)

      i += 1

   merged.append([start, end])

   while i< N:
      merged.append(intervals[i])
      i+= 1

   return merged 


def main():
   Intervals=[[1,3], [5,7], [8,12]] 
   New_Interval=[4,6]
   inserted = insert_interval(Intervals, New_Interval)
   print("Inserted {0} to {1} result in {2}".format(New_Interval, Intervals, inserted))

   Intervals=[[1,3], [5,7], [8,12]] 
   New_Interval=[4,10]
   inserted = insert_interval(Intervals, New_Interval)
   print("Inserted {0} to {1} result in {2}".format(New_Interval, Intervals, inserted))

   Intervals=[[2,3],[5,7]] 
   New_Interval=[1,4]
   inserted = insert_interval(Intervals, New_Interval)
   print("Inserted {0} to {1} result in {2}".format(New_Interval, Intervals, inserted))

if __name__ == "__main__":
   main()

