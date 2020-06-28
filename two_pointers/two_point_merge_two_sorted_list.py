
'''
Merge two sorted linked list

Given 2 sorted linked list merge them into one sorted list and return the head.
'''

class Node:
   def __init__(self, val):
      self.val = val
      self.next = None


def mergelist(l1, l2):
   if not l1: return l2
   if not l2: return l1

   fake = Node(-1) # like a head
   last = fake  # like a tail
   while l1 and l2:
      if l1.val <= l2.val:
         last.next = l1
         last = l1
         l1 = l1.next 
      else:
         last.next = l2
         last = l2
         l2 = l2.next 
   
   if not l2:
      last.next = l1
   if not l1:
      last.next = l2
   
   return fake.next


def display(head):
   temp = head

   while temp:
      print(temp.val, end=" ")
      temp = temp.next 
   print()

def main():
   l1 = Node(2)
   l1.next = Node(4)
   l1.next.next = Node(6)
   l1.next.next.next = Node(8)
   l1.next.next.next.next = Node(10)

   l2 = Node(1)
   l2.next = Node(3)
   l2.next.next = Node(5)
   l2.next.next.next = Node(7)
   l2.next.next.next.next = Node(9)

   print("List one:", end=" ")
   display(l1)
   print("list two:", end=" ")
   display(l2)
   print("Merged List:", end=" ")
   display(mergelist(l1,l2))



if __name__ == "__main__":
   main()

