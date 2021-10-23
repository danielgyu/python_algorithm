def solution(prices: list) -> int:
    if len(prices) < 2:
        return 0

    max_profit = 0
    buy = 0

    for i in range(1, len(prices)):
        max_profit = max(max_profit, prices[i] - prices[buy])
        if prices[i] < prices[buy]:
            buy = i

    return max_profit


print(solution([7, 1, 5, 3, 6, 4]))
print(solution([7, 6, 4, 3, 1]))
