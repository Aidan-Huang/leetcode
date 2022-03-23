from typing import List

# 买卖股票的最佳时机 II
def test122():
    def maxProfit(prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        profit = 0
        buy = 0
        sell = 1

        while sell < n:
            if prices[sell] < prices[buy]:
                buy += 1
            elif sell < n - 1 and prices[sell + 1] < prices[sell]:
                profit += prices[sell] - prices[buy]
                sell += 1
                buy = sell
            elif sell == n - 1:
                profit += prices[sell] - prices[buy]

            sell += 1

        return profit

    def maxProfit0(prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        profit = 0

        for index in range(1, n):
            if prices[index] > prices[index - 1]:
                profit += prices[index] - prices[index - 1]

        return profit

    prices = [7, 1, 5, 3, 6, 4]
    assert maxProfit0(prices) == 7

    prices = [1, 2, 3, 4, 5]
    assert maxProfit0(prices) == 4

    prices = [0]
    assert maxProfit0(prices) == 0

    prices = [1]
    assert maxProfit0(prices) == 0
