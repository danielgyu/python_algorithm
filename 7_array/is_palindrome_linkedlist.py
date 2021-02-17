# https://leetcode.com/problems/palindrome-linked-list/

def is_palindrome(head):
    from collections import deque
    
    if not head:
        return True
    
    q = deque()
    
    node = head
    while node is not None:
        q.append(node.val)
        node = node.next
    
    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
    
    return True
