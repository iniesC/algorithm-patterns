
'''
Problem Statement 
Given the head of a LinkedList and two positions ‘p’ and ‘q’, 
reverse the LinkedList from position ‘p’ to ‘q’.
'''

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()

def reverse_sublist(head, p, q):
   if not head or p == q:
      return head
   
   prev = None
   curr = head

   cnt = 0
   while curr and cnt < p-1:
      prev = curr
      curr = curr.next 
      cnt += 1

   last_node_of_first_part = prev
   last_node_of_sub_list = curr
   
   n = None
   cnt = 0
   while curr and cnt < q-p+1:
      n = curr.next 
      curr.next = prev
      prev = curr
      curr = n 
      cnt += 1
   
   if not last_node_of_first_part:
      head = prev
   else:
      last_node_of_first_part.next = prev
   
   last_node_of_sub_list.next = curr

   return head



def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
   
  head = reverse_sublist(head, 2, 4)
  head.print_list()

if __name__ == "__main__":
   main()

