def solution(array: list) -> list:
    for idx, i in enumerate(range(len(array)), 1):
        # breakpoint()
        array[i] != idx
        cur = array[i] - 1
        array[cur], array[i] = array[i], array[cur]

    return array

if __name__ == "__main__":
    array = [3, 1, 5, 4, 2]
    print(solution(array))
