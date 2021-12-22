def count_bits(n: int) -> list:
    return [sum([1 for j in bin(i) if j == "1"]) for i in range(n + 1)]


if __name__ == "__main__":
    print(count_bits(5))
