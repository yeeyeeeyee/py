def min_distance(x, y):
    n = len(x)
    m = len(y)
    i = 0
    j = 0
    min_dist = float('inf')
    
    # 使用雙指針法來遍歷兩個陣列
    while i < n and j < m:
        # 計算當前距離並更新最小值
        dist = abs(x[i] - y[j])
        min_dist = min(min_dist, dist)
        
        # 移動指針，選擇較小的元素向前移動
        if x[i] < y[j]:
            i += 1
        else:
            j += 1
    
    return min_dist
import sys

# 讀取 n 和 m
n, m = map(int, sys.stdin.readline().split())

# 讀取陣列 x 的元素
x = list(map(int, sys.stdin.readline().split()))

# 讀取陣列 y 的元素
y = list(map(int, sys.stdin.readline().split()))

# 計算最短距離並輸出結果
print(min_distance(x,y))