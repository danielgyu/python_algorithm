def solution(array: list):
    max_sum = array[0] + array[1]
    current_sum = max(max_sum, array[1])

    for i in range(2, len(array)):
        current_sum = max(current_sum, current_sum + array[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

if __name__ == "__main__":
    array = [8, 5, 12, 9, 19, 1]
    print(solution(array))
