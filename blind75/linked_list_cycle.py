class ListNode:
     def __init__(self, x, n=None):
         self.val = x
         self.next = n 

def has_cycle(head: ListNode) -> bool:
    mapper = {}
    while head:
        if mapper.get(head.val) and head == mapper[head.val]:
            return True 

        mapper[head.val] = head

        head = head.next

    return False

if __name__ == "__main__":
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2

    m1 = ListNode(3)
    m2 = ListNode(2)
    m3 = ListNode(0)
    m1.next = m2
    m2.next = m3

    print(has_cycle(n1))
    print(has_cycle(m1))
