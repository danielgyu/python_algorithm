def get_minimum(lst: list) -> int:
    n = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < n:
            n = lst[i]

    return n


def merge_sort(lst: list) -> None:
    if len(lst) > 1:
        middle = len(lst) // 2
        left = lst[:middle]
        right = lst[middle:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
    
        while (i < len(left)) and (j < len(right)):

            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            
            else:
                lst[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1


def use_sort(lst: list) -> int:
    merge_sort(lst)
    return lst[0]


if __name__ == "__main__":
    print(get_minimum([3, 1, 9, 2, 0]))
    print(use_sort([3, 1, 9, 2, 0]))
