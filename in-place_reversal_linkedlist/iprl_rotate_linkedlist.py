
'''
Rotate a LinkedList (medium) #
Given the head of a Singly LinkedList and a number ‘k’, 
rotate the LinkedList to the right by ‘k’ nodes.
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


def rotate(head, k):
   if not head:
      return head
   
   length = 0
   temp = head
   lastNode = None
   while temp:
      length += 1
      lastNode = temp
      temp = temp.next
   
   rotate_len = k % length
   cnt = 0
   prev = None
   curr = head

   while curr and cnt < length-rotate_len:
      prev = curr
      curr = curr.next

      cnt += 1
   
   prev.next = lastNode.next
   lastNode.next = head
   head = curr

   

   return head
   

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = rotate(head, 3)
  print("Nodes of rotated LinkedList are: ", end='')
  result.print_list()

  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = rotate(head, 8)
  print("Nodes of rotated LinkedList are: ", end='')
  result.print_list()


if __name__ == "__main__":
   main()

