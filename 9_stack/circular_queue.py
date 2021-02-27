# https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:
    """
    순환형 큐를 디자인하는 문제이다.
    큐의 사이즈는 fix된 상태이고, 포인터 두개로 Front와 Rear를 기록한다.
    """

    def __init__(self, k: int):
        self.queue = [None] * k
        self.size = k
        self.p1 = 0
        self.p2 = 0

    def enQueue(self, value: int) -> bool:
        if self.queue[self.p2] is None:
            self.queue[self.p2] = value
            self.p2 = (self.p2 + 1) % self.size
            return True
        return False

    def deQueue(self) -> bool:
        if not self.queue[self.p1] is None:
            self.queue[self.p1] = None
            self.p1 = (self.p1 + 1) % self.size
            return True
        return False
        
    def Front(self) -> int:
        """
        하나 명심해야 하는건 queue라는 것이다.
        따라서 front는 리스트의 맨 뒤가 아닌 앞을 의미한다.
        """
        if self.queue[self.p1] is None:
            return False
        return self.queue[self.p1]

    def Rear(self) -> int:
        """
        1을 빼는 이유는 현재 self.p2는 하나 더해진 상태이다(enqueue를 할 때 비었는지 확인하기 위해)
        """
        if self.queue[self.p2 - 1] is None:
            return False
        return self.queue[self.p2 - 1]
        
    def isEmpty(self) -> bool:
        return (self.p1 == self.p2) and (self.queue[self.p1] is None)

    def isFull(self) -> bool:
        return (self.p1 == self.p2) and (self.queue[self.p2] is not None)