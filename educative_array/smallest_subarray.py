from collections import deque
from typing import Union


def solution(array: list, k: int) -> Union[list, int]:
    smallest_sum = 0
    answer_array = list()
    managed_array = list()

    for i in range(len(array)):
        current_num = array[i]

        if current_num == k:
            return [current_num]

        managed_array.append(current_num)
        current_sum = sum(managed_array)

        if current_sum >= k and current_sum < smallest_sum:
            smallest_sum = current_sum
            answer_array = managed_array[:]
        elif current_sum >= k and current_sum >= smallest_sum:
            managed_array.pop(0)
            if sum(managed_array) >= k:
                answer_array = managed_array[:]

    return answer_array if answer_array else 0


if __name__ == "__main__":
    v1, k1 = [2, 1, 5, 2, 3, 2], 7
    v2, k2 = [2, 1, 5, 2, 8], 8
    v3, k3 = [3, 4, 1, 1, 6], 8
    print(solution(v1, k1))
    print(solution(v2, k2))
    print(solution(v3, k3))
