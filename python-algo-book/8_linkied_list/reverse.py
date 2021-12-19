# https://leetcode.com/problems/reverse-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list_recursion(head):
    """
    재귀형식으로 연결 리스트를 거꾸로 뒤집는 방법이다.
    prev=None을 통해서 뒤집히는 연결 리스트를 담을 변수를 생성한다.
    그리고 정확히 어떻게 뒤바뀌게 되는지는 iteration을 보면 조금 더 쉽게 이해할 수 있다.
    -
    """
    
    def reverse(node, prev=None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)


def reverse_list_iteration(head):
    """
    prev, node = node, next 이 라인이 재귀에서는 빠져 있는데,
    prev가 node로 교체되는걸 알 수 있다.
    하지만 이 node의 next는 이미 위에서 prev로 대체됐기 때문에, 처음 시작할때는 None이 된다.
    그러고 node는 next로 바꿔주면,
    prev는 next가 없어진(첫 iteration에) node가 되었고, node는 원래 다음 값으로 넘어갔다.
    다음 반복에서 node.next는 그전 prev인 next가 None인 node이다.
    결국 prev를 반화할때 prev는 새로 만들어져서 이어지는게 아니라,
    사실 뒤집고 값이 변하는건 node라는 변수 안에서 이뤄진다.
    """
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next
    
    return prev