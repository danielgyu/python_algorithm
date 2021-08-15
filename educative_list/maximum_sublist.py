def get_maximum_sublist(lst: list) -> int:
    max_sum = lst[0]
    current_sum = max_sum

    for i in range(1, len(lst)):
        current_sum = max(lst[i], current_sum + lst[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    lst = [-2, 10, 7, -5, 15, 6]
    print(get_maximum_sublist(lst))
