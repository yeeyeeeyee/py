import sys
N = int(sys.stdin.readline()) # 讀取 N 的值

# 繪製樹冠
for i in range(N):
    print(' ' * (N - i - 1) + '*' * (2 * i + 1))

# 繪製樹幹
for i in range(N-1):
    print(' ' * (N - 1) + '|')