
'''
Problem Statement #
Given the head of a Singly LinkedList that contains a cycle, 
write a function to find the starting node of the cycle.
'''
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def cycle_length(node):
   if not node:
      return 0

   p1 = node
   p2 = p1.next
   cnt = 1
   while p2 and p1 != p2:
      cnt +=1
      p2 = p2.next
   
   return cnt if p1 == p2 else 0

def find_start(head):

   # Step 1: find the length of the cycle
   slow = fast = head
   cycle_len = 0
   while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

      if slow == fast:
         cycle_len = cycle_length(slow)
         break
   
   # Step2  move the two pointers apart cycle length
   p1 = p2 = head
   while cycle_len > 0 and p2:
      p2 = p2.next
      cycle_len -= 1
   
   # Step 3: move the pointers until the meet at the cycle start
   while p1 != p2:
      p1 = p1.next
      p2 = p2.next

   return p1


def main():
   head = Node(1)
   head.next = Node(2)
   head.next.next = Node(3)
   head.next.next.next = Node(4)
   head.next.next.next.next = Node(5)
   head.next.next.next.next.next = Node(6)

   head.next.next.next.next.next.next = head.next.next
   print("LinkedList cycle start: " + str(find_start(head).value))

   head.next.next.next.next.next.next = head.next.next.next
   print("LinkedList cycle start: " + str(find_start(head).value))

   head.next.next.next.next.next.next = head
   print("LinkedList cycle start: " + str(find_start(head).value))


if __name__ == "__main__":
   main()

