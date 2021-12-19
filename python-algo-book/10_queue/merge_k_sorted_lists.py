# https://leetcode.com/problems/merge-k-sorted-lists/submissions/

from typing import List
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    """
    정렬된 k개의 linked list를 연결하는 문제고, 힙을 통해 해결한다.
    """
    
    # result로 정렬을 하기 때문에, 계속 next가 콜링이 된다
    # root로 원래 자리를 지키면 result와 같은 객체를 포인트해준다
    root = result = ListNode(None)
    heap = []
    
    for i in range(len(lists)):
        # 먼저 heap이라는 배열안에 모든 linkedlist를 넣어준다
        if lists[i]:
            # 인덱스를 넣는 이유는 힙은 중복된 값을 집어넣지 못하기 때문이다
            # lists[i].val을 넣으면 가장 작은 숫자를 가진 리스트로 힙안에서 정렬이 된다
            heapq.heappush(heap, (lists[i].val, i, lists[i]))
    
    while heap:
        # 힙에서 가장 작은 리스트를 팝한다
        node = heapq.heappop(heap)
        idx = node[1]
        # 이 next를 하는 이유는 우리가 이미 None값을 가진 리스트노드를 위에 가졌기 때문에
        result.next = node[2]
        
        # 이렇게 보면 result.next가 두번째 아이템 같아 보이지만 실상 리스트의 첫 아아템이다
        result = result.next
        if result.next:
            heapq.heappush(heap, (result.next.val, idx, result.next))
    
    # 처음 선언한 None값인 노드를 제외한 다음노드부터
    return root.next