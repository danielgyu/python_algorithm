def find_second_maximum(lst: list) -> int:
    first = second = 0
    
    for i in range(2, len(lst)):

        if lst[i] >= first:
            second = first
            first = lst[i]

        elif first > lst[i] >= second:
            second = lst[i]

    return second

if __name__ == "__main__":
    print(find_second_maximum([4, 9, 3, 19, 6, 11, 29, 17, 18]))
