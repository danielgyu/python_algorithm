# https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    """
    """
    l3 = ListNode()

    while l1 and l2:
        if l1.val < l2.val:
            l3.val = l1.val
            l1 = l1.next
        else:
            l3.val = l2.val
            l2 = l2.next
        l3.next = ListNode()
        l3 = l3.next


    