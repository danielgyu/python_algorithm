from collections import deque

def get_maximum_sublist(lst: list) -> int:
    max_sum = lst[0]
    buf = deque()

    for i in range(1, len(lst)):
        if not buf:
            current_max = max(lst[i], lst[i-1] + lst[i])
        else:
            buf.append(lst[i])
            current_max = max(lst[i], buf)

        if current_max > max_sum:
            max_sum = current_max


if __name__ == "__main__":
    lst = [-2, 10, 7, -5, 15, 6]
    print(get_maximum_sublist(lst))
