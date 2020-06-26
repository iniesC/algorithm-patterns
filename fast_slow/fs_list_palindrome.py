
'''
Check if Linked List is Palindrome or not

Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished. The algorithm should have O(N)O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.

Example 1:

Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
Output: true
Example 2:

Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
Output: false
'''
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def find_middle_node(head):
   slow = fast = head
   while fast and fast.next:
      slow = slow.next 
      fast = fast.next.next 
   
   return slow

def reverse(node):
   prev = None
   curr = node

   n = None
   while curr:
      n = curr.next 
      curr.next = prev 
      prev = curr
      curr = n
   
   return prev

def is_palindrome(head):
   if not head:
      return True

   # fidn middle node
   middle_node = find_middle_node(head)
   # reverse from middle node
   second_head = reverse(middle_node)
   copy_second_head = second_head

   # compare left-to-middle list to right-to-middle list
   while head and second_head:

      if head.value != second_head.value:
         break
      
      head = head.next
      second_head = second_head.next 
   
   # reverse second half back to original state
   reverse(copy_second_head)

   if head or second_head:
      return False
   
   return True




def main():
   head = Node(2)
   head.next = Node(4)
   head.next.next = Node(6)
   head.next.next.next = Node(4)
   head.next.next.next.next = Node(2)

   print("Is palindrome: " + str(is_palindrome(head)))

   head.next.next.next.next.next = Node(2)
   print("Is palindrome: " + str(is_palindrome(head)))



if __name__ == "__main__":
   main()

