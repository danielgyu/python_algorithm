def rearrange_in_max_min(lst: list) -> list:
    length = len(lst)
    final = [0 for i in range(length)]
    sorted_list = sorted(lst)
    
    i, left, right = 0, 0, length - 1
    while left <= right:
        if i % 2 == 0:
            final[i] = sorted_list[right]
            right -= 1
        else:
            final[i] = sorted_list[left]
            left += 1
        i += 1

    return final

if __name__ == "__main__":
    lst1 = [15, 1, 3, 9, 12, 19]
    print(rearrange_in_max_min(lst1))
    lst2 = [1, 2, 3, 4, 5] 
    print(rearrange_in_max_min(lst2))
