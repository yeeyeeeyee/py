def knapsack(N: int, W: int, items: [(int,int)]) -> int:
    """
    N: 物品數量
    W: 背包能夠承受的重量
    items: 一個元組列表，每個元組包含物品的重量和價值
    返回值：小偷最多能偷到多少價值的東西
    """
    
    # 創建一個二維數組 dp，dp[i][j] 表示考慮前 i 個物品，背包容量為 j 時能夠偷到的最大價值
    dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
    
    # 遍歷每一件物品
    for i in range(1,N+1):
        # 遍歷每種可能的背包容量
        for j in range(1,W+1):
            # 如果當前物品重量大於背包容量，則不選擇當前物品
            if items[i-1][0] > j:
                dp[i][j] = dp[i-1][j]
            else:
                # 否則，在選擇當前物品和不選擇當前物品中選擇價值較大者
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-items[i-1][0]] + items[i-1][1])
    
    return dp[N][W]