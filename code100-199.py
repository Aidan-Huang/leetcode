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

    prices = [7,1,5,3,6,4]
    assert maxProfit(prices) == 7