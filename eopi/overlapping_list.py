class Node:
    def __init__(self, next = None):
        self.next = next

def overlapping(L1, R1):

    def get_length(node):
        length = 0
        while node:
            length += 1
            node = node.next

        return length

    L1_length = get_length(L1)
    R1_length = get_length(R1)

    if L1_length > R1_length:
        R1, L1 = L1, R1

    for _ in range(R1_length - L1_length):
        R1 = R1.next

    while (L1 and R1) and (L1 != R1):
        L1 = L1.next
        R1 = R1.next

    return L1

if __name__ == "__main__":
    l1 = Node()
    l2 = Node()
    l3 = Node()
    l4 = Node()
    r1 = Node()
    r2 = Node()

    l1.next = l2
    l2.next = l3
    l3.next = l4

    r1.next = r2
    r2.next = l2

    print(overlapping(l1, r1))

    z1 = Node()
    z2 = Node()
    z3 = Node()
    x1 = Node()
    x2 = Node()

    print(overlapping(z1, x2))

