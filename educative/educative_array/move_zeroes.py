def solution(array: list) -> list:
    read = len(array) - 1
    write = read

    while read >= 0:
        if array[read] == 0:
            read -= 1
            continue
        else:
            array[write] = array[read]
            read -=1
            write -= 1

    while write >= 0:
        array[write] = 0
        write -= 1

    return array

if __name__ == "__main__":
    array= [1, 10, 20, 0, 59, 63, 0, 88, 0]
    print(solution(array))
