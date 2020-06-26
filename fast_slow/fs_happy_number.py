
'''
Happy Number

Any number will be called a happy number if, after repeatedly replacing it 
with a number equal to the sum of the square of all of its digits, 
leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. 
Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

Example 1:

Input: 23   
Output: true (23 is a happy number)  

Example 2:

Input: 12   
Output: false (12 is not a happy number)  
'''
def find_squares(num):
   sum = 0

   while num:
      sum += pow(num%10, 2)
      num = num//10
   
   return sum

def isHappyNumber(num):
   slow = fast = num

   while fast != 1:
      slow = find_squares(slow)
      fast = find_squares(find_squares(fast))

      if slow == fast:
         return False
   
   return True

def main():
   num = 23
   print("Number '{0}' is happy number: {1}".format(num,isHappyNumber(num)))

   num = 12
   print("Number '{0}' is happy number: {1}".format(num,isHappyNumber(num)))


if __name__ == "__main__":
   main()

