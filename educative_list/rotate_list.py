def right_rotate_list(n: int, lst: list) -> list:
    for i in range(n):
        m = lst.pop()
        lst = [m] + lst

    return lst

if __name__ == "__main__":
    print(right_rotate_list(3, [1, 2, 3, 4, 5]))
