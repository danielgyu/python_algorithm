def merge_two_sorted_list(l1: list, l2: list) -> list:
    i = j = 0
    final = []

    while len(final) < (len(l1) + len(l2)):
        if i < len(l1) and j < len(l2):
            if l1[i] > l2[j]:
                final.append(l2[j])
                j += 1
            elif l2[j] > l1[i]:
                final.append(l1[i])
                i += 1
            else:
                final.append(l1[i])
                i += 1
        elif i < len(l1):
            final.append(l1[i])
            i += 1
        else:
            final.append(l2[j])
            j += 1

    return final


def merge_in_place(l1: list, l2: list) -> list:
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] > l2[j]:
            l1.insert(i, l2[j])
            i += 1
            j += 1
        else:
            i += 1

    if j < len(l2):
        l1.extend(l2[j:])
    
    return l1

if __name__ == "__main__":
    l1 = [1, 3, 4, 5]
    l2 = [2, 6, 7, 8]
    print(merge_two_sorted_list(l1, l2))
    print(merge_in_place(l1, l2))
