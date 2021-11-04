import collections

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors

    def __repr__(self):
        return "node value:" + str(self.val)

def dfs(node: Node) -> Node:
    c = {node: Node(node.val, [])}
    stack = [node]

    while stack:
        n = stack.pop()
        for neighbor in n.neighbors:
            if neighbor not in c:
                c[neighbor] = Node(neighbor.val, [])
                stack.append(neighbor)
            c[n].neighbors.append(c[neighbor])

    return c[node]


def bfs(node: Node) -> Node:
    c = {node: Node(node.val, [])}
    deque = collections.deque([node])

    while deque:
        d = deque.popleft()
        for neighbor in d.neighbors:
            if neighbor not in c:
                d.append(neighbor)
                c[neighbor] = Node(neighbor.val)
            c[d].neighbors.append(c[neighbor])

    return c[node]


if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    a.neighbors = [b, d]
    b.neighbors = [a, c]
    c.neighbors = [b, d]
    d.neighbors = [a, c]

    res = dfs(a)
