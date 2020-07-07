
'''
Problem Statement 
Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

Example 1:

Appointments: [[1,4], [2,5], [7,9]]
Output: false
Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.
Example 2:

Appointments: [[6,7], [2,4], [8,12]]
Output: true
Explanation: None of the appointments overlap, therefore a person can attend all of them.
Example 3:

Appointments: [[4,5], [2,3], [3,6]]
Output: false
Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.
 
'''

def can_attend(intervals):
   if len(intervals) == 0:
      return True
   
   start, end = 0, 1
   intervals.sort(key=lambda x: x[0])

   for i in range(1,len(intervals)):
      prev = intervals[i-1]
      curr = intervals[i]

      if curr[start] < prev[end]:
         return False
   
   return True

def main():
   intervals = [[1,4], [2,5], [7,9]]
   print("Is there is a conflict with {0}: {1}".format(intervals, can_attend(intervals)))

   intervals = [[6,7], [2,4], [8,12]]
   print("Is there is a conflict with {0}: {1}".format(intervals, can_attend(intervals)))

   intervals = [[4,5], [2,3], [3,6]]
   print("Is there is a conflict with {0}: {1}".format(intervals, can_attend(intervals)))



if __name__ == "__main__":
   main()

