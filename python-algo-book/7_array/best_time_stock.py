# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(prices):
    """
    가장 큰 이익을 찾아서 반환하는 문제.
    따로 날짜는 없기 때문에 그냥 가장 큰 차익 값만 구하면 된다.
    이익이 안나올 경우 0을 반환.
    """
    max_profit = 0
    low = prices[0]

    for price in prices:
        if price < low:
            low = price
        else:
            profit = price - low
            if profit > max_profit:
                max_profit = profit

    return max_profit

def maxProfit2(prices):
    """
    조금 더 간결한 코드로 적용해 본다
    """
    import sys
    max_profit = 0
    min_price = sys.maxsize

    for price in prices:
        min_price = min(price, min_price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

prices = [7,1,5,3,6,4]
prices2 = [5,4,3,2,1]
print(maxProfit(prices), maxProfit(prices2))
print(maxProfit2(prices), maxProfit2(prices2))