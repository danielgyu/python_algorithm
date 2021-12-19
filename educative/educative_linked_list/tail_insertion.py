from linked_list import LinkedList
from node import Node

# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Node class  {int data ; Node next_element;}

# Inserts a value at the end of the list
def insert_at_tail(lst, value):
    tail_node = LinkedList(value, None)

    if lst.is_empty():
        return tail_node

    head = lst.get_head()
    node = head
    while node.next is not None:
        node = node.next

    node.next = tail_node

    return head
