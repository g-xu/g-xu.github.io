#股票系列问题的状态机算法 参考 https://leetcode-cn.com/circle/article/qiAgHn/

# T[i][k][0|1] T表示收益，i表示第几天 K表示第几次操作 0|1表示手里是否有股票
# base status
# T[-1][k][0] = 0, T[-1][k][1] = -Infinity
# T[i][0][0] = 0, T[i][0][1] = -Infinity
# 状态转移方程
# T[i][k][0] = max(T[i - 1][k][0], T[i - 1][k][1] + prices[i])
# T[i][k][1] = max(T[i - 1][k][1], T[i - 1][k - 1][0] - prices[i])


def max_profit_k1(price):
    
    total = len(price)
    dp = [[0,-price[0]],]
    for i in range(1, total):
        p0 = max(dp[i-1][0], dp[i-1][1]+price[i])
        p1 = max(dp[i-1][1], -price[i])
        dp.append([p0, p1])
    
    return dp[total-1][0]


if __name__ == '__main__':
    profit = max_profit_k1([7,1,5,3,6,4])
    profit = max_profit_k1([7,6,4,3,1])
    profit = max_profit_k1([7,1,5,3,4,6])


    print(profit)