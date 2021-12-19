import math


def find_list_of_products(l1: list) -> list:
    total_product = math.prod(l1)
    for i in range(len(l1)):
        l1[i] = total_product // l1[i]

    return l1


if __name__ == "__main__":
    l1 = [1, 2, 3, 4]
    print(find_list_of_products(l1))
