# https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:
    """
    큐를 이용해 스택을 구현하는 문제이다.
    그 의미는, MyStack은 FIFO하는 구조여야만 한다는 뜻이다.
    """

    def __init__(self):
        from collections import deque
        self.stack = deque()
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        """
        여기서 따로 for문을 해주는 이유는 FIFO하는 큐의 특성을 유지하기 위해서이다.
        push를 통해 추가된 아이템 이외의 모든 아이템들을 하나씩 popleft하면서 뒤로 옮긴다.
        """
        for _ in range(len(self.stack) - 1):
            self.stack.append(self.stack.popleft())
        

    def pop(self) -> int:
        return self.stack.popleft()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[0]
        

    def empty(self) -> bool:
        return len(self.stack) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()