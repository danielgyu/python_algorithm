def ideal(l1: list, l2: list, l3: list) -> int:
    i = j = k = 0

    while i < len(l1) and j < len(l2) and k < len(l3):

        if l1[i] == l2[j] == l3[k]:
            return l1[i]

        if l1[i] < l2[j] and l1[i] < l3[k]:
            i += 1

        elif l2[j] < l1[i] and l2[j] < l3[k]:
            j += 1

        elif l3[k] < l1[i] and l3[k] < l2[j]:
            k += 1

    return -1


def solution(l1: list, l2: list, l3: list) -> int:
    i = j = k = 0

    while i < len(l1) and j < len(l2) and k < len(l3):

        if l1[i] == l2[j] == l3[k]:
            return l1[i]

        if l1[i] > l2[j] :
            if l1[i] > l3[k]:
                j += 1
                k += 1
            else:
                j += 1

        elif l2[j] > l3[k]:
            if l2[j] > l1[i]:
                i += 1
                k ++ 1
            else:
                k += 1

        elif l3[k] > l1[i]:
            if l3[k] > l2[j]:
                j += 1
                i += 1
            else:
                i += 1

    return -1

if __name__ == "__main__":
    l1 = [6, 7, 10, 25, 30, 63, 65]
    l2 = [0, 4, 5, 6, 7, 8, 50]
    l3 = [1, 6, 10, 14]
    m1 = [100, 101, 102]
    m2 = [99, 102, 105]
    m3 = [76, 88, 102]
    n1 = [1, 2]
    n2 = [3, 4]
    n3 = [5, 6]
    print(solution(l1, l2, l3))
    print(solution(m1, m2, m3))
    print(solution(n1, n2, n3))
    print("")
    print(ideal(l1, l2, l3))
