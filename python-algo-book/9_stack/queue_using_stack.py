# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:
    """
    스택을 활용해 큐를 구현하는 문제다.
    두 개의 스택을 활용해서 들어오는건 input으로 받고,
    나갈 때는 output에서 빼가는데, 만약에 output이 없을 경우에는 
    그 시점에 input에 있는 아이템들을 전부 옮겨준다.
    """

    def __init__(self):
        self.input = []
        self.output = []
        

    def push(self, x: int) -> None:
        self.input.append(x)
        

    def pop(self) -> int:
        self.peek()
        return self.output.pop()
        

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
        

    def empty(self) -> bool:
        return len(self.input) == 0 and len(self.output) == 0
