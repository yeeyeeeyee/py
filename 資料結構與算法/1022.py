import sys
N = int(sys.stdin.readline())

for i in range(1, N+1):
    # 計算每一層需要印出的空格數
    spaces = ' ' * (N-i)
    # 計算每一層需要印出的星號數
    stars = '*' * (2*i-1)
    # 輸出每一層
    print(spaces + stars)