from typing import List


# 买卖股票的最佳时机 II
def test122():
    # Aidan
    # 买入点：没遇到涨，买入点就前移，直到最后一天
    # 卖出点：买入过，遇到跌，前一天肯定是卖出点，交易
    # 边界：最后一天是涨的话，第二条件不满足，（只确认了买入点，还没遇到跌的情况），交易
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

    # Eric
    # 分析折线图
    # 买入点：一个点左边平或者高，右边高，就是买入点，记录
    # 卖出点：一个点左边平或者低，右边低，就是买出点，记录
    # 边界：判断第一天是否买入点，判断最后一天是否卖出点
    #      卖出点前必定存在买入点
    # 结算：依次交易，返回累积收益
    def maxProfit1(prices):

        buy = []
        sell = []
        n = len(prices)
        if n < 2:
            return 0
        i = 0
        profit = 0
        while i <= n - 1:
            if i == 0 and prices[i] <= prices[i + 1] and len(buy) == len(sell):
                buy.append(prices[i])
            if i != n - 1 and i != 0:
                if prices[i] <= prices[i - 1] and prices[i] <= prices[i + 1] and len(buy) == len(sell):
                    buy.append(prices[i])
                if prices[i] >= prices[i + 1] and prices[i] >= prices[i - 1] and len(buy) == len(sell) + 1:
                    sell.append(prices[i])
            if i == n - 1 and prices[i] >= prices[i - 1] and len(buy) == len(sell) + 1:
                sell.append(prices[i])
            i += 1

        for num in range(len(sell)):
            profit += sell[num - 1] - buy[num - 1]

        return profit


    # 官方算法
    # 贪心法，遇到涨就结算当地的收益，返回累计收益
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
    assert maxProfit1(prices) == 7

    prices = [1, 2, 3, 4, 5]
    assert maxProfit1(prices) == 4

    prices = [2, 2, 5]
    assert maxProfit1(prices) == 3

    prices = [1, 1, 0]
    assert maxProfit1(prices) == 0

    prices = [8, 6, 4, 3, 3, 2, 3, 5, 8, 3, 8, 2, 6]
    assert maxProfit1(prices) == 15

    prices = []
    assert maxProfit1(prices) == 0

    prices = [1]
    assert maxProfit1(prices) == 0
