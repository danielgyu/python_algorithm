# https://leetcode.com/problems/design-circular-deque/

class ListNode:
    
    def __init__(self, val):
        self.val = val


class MyCircularDeque:

    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head
        
    def _add(self, node, new):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new

    def _delete(self, node):
        n = node.right.right
        node.right = n
        n.left = node

    def insertFront(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True
        

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._delete(self.head)
        return True
        

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._delete(self.tail.left.left)
        return True
        

    def getFront(self) -> int:
        if self.len:
            return self.head.right.val
        return -1
        

    def getRear(self) -> int:
        if self.len:
            return self.tail.left.val
        return -1
        

    def isEmpty(self) -> bool:
        return self.len == 0
        

    def isFull(self) -> bool:
        return self.len == self.k