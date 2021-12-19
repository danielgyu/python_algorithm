def remove_even_int_from_list(lst: list) -> list:
    output_list = []
    for l in lst:
        if l % 2 == 0:
            output_list.append(l)

    return output_list


if __name__ == "__main__":
    input_list = [1, 2, 4, 5, 9]
    print(remove_even_int_from_list(input_list))
    print([l for l in input_list if l % 2 == 0])
