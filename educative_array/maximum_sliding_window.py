from collections import deque

def attempt(nl: list, k: int) -> deque:
    res = deque()
    window = deque()

    for i in range(k):
        if window:
            window = deque([w for w in window if nl[w] >= nl[i]])

        window.append(i)
    
    res.append(max([nl[n] for n in window]))

    for i in range(k, len(num_list)):
        if window:
            window = deque([w for w in window if nl[w] >= nl[i]])

        window.append(i)
        res.append(max([nl[n] for n in window]))
    
    return res

def solution(nl: list, k: int) -> list:
    res = []
    window = deque()

    for i in range(k):
        while window and nl[i] >= nl[window[-1]]:
            window.pop()
        window.append(i)

    res.append(nl[window[0]])

    for i in range(k, len(nl)):
        while window and nl[i] >= nl[window[-1]]:
            window.pop()

        if window and (window[0] <= i - k):
            window.popleft()

        window.append(i)
        res.append(nl[window[0]])

    return res


if __name__ == "__main__":
    num_list = [-4, 2, -5, 1, -1, 6]
    k = 3
    print(solution(num_list, k))
