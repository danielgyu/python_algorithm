def reverse(n: int) -> int:
    result, remaining = 0, abs(n)
    while remaining > 0:
        result = (result * 10) + (remaining % 10)
        remaining //= 10

    return result if n > 0 else result * -1


print(reverse(1139))
print(reverse(12345))
print(reverse(-321))
