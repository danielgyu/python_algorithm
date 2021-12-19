def rearrange_numbers(lst: list) -> list:
    idx = 0

    for i in range(len(lst)):
        if lst[i] < 0:
            lst[idx], lst[i] = lst[i], lst[idx]
            idx += 1

    return lst

if __name__ == "__main__":
    lst = [10,-1,20,4,5,-9,-6]
    print(rearrange_numbers(lst))

