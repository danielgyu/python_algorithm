def hamming_weight(n: int) -> int:
    return sum([1 for b in bin(n) if b == "1"])


if __name__ == "__main__":
    print(hamming_weight(11))
