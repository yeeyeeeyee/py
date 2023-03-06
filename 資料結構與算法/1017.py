import sys

C = int(sys.stdin.readline()) # 讀取小偷最多能夠帶走幾樣物品
N = int(sys.stdin.readline()) # 讀取一共有幾項物品
P = [] # 創建一個空列表來存儲每樣物品的價值
for i in range(N):
    P.append(int(sys.stdin.readline())) # 讀取每樣物品的價值並添加到列表中

P.sort(reverse=True) # 將物品價值按照降序排列

max_value = 0 # 初始化最大價值為 0
for i in range(min(C,N)): # 選擇前 C 個物品（如果物品數量小於 C，則選擇所有物品）
    max_value += P[i] # 計算選擇的物品的總價值

print(max_value) # 輸出最大價值