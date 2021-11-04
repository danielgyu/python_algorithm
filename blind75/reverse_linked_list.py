import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(node: ListNode) -> ListNode:
    deque = collections.deque()
    while node:
        deque.append(ListNode(node.val))
        node = node.next

    node = deque.popleft()
    while deque:
        p = deque.popleft()
        p.next = node
        node = p

    return node


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    a.next = b
    b.next = c
    c.next = d

    rl = reverse_list(a)
