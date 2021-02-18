# https://leetcode.com/problems/palindrome-linked-list/

def is_palindrome(head):
    """
    deque를 활용한 풀이
    """
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


def is_plaindrome(head):
    """
    런너를 활용한 풀이
    """
    rev = None
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    while rev and (rev.val == slow.val):
        rev = rev.next
        slow = slow.next
    
    return not rev
