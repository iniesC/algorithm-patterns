
'''
Problem Statement #
Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.

If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.
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

def reverse_every_k_elements(head, k):
   if not head or k == 0:
      return head
   
   prev, curr = None, head

   while curr:

      last_node_first_sublist = prev
      last_node_sublist = curr

      cnt = 0
      while curr and cnt < k:
         n = curr.next
         curr.next = prev
         prev = curr
         curr = n 

         cnt += 1

      if last_node_first_sublist:
         last_node_first_sublist.next = prev
      else:
         head = prev
      
      last_node_sublist.next = curr
      prev = last_node_sublist
   
   return head

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.next.next = Node(8)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_every_k_elements(head, 3)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()

if __name__ == "__main__":
   main()

