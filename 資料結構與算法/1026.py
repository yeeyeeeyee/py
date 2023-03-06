import sys
# 輸入N
N = int(sys.stdin.readline())

# 輸入數列
sequence = list(map(int, sys.stdin.readline().split()))

# 判斷是否為等比數列
is_geometric = True
if sequence[0] == 0:
    is_geometric = all(x == 0 for x in sequence)
else:
    common_ratio = sequence[1] / sequence[0]
    for i in range(1, N):
        if sequence[i-1] == 0 or sequence[i] / sequence[i-1] != common_ratio:
            is_geometric = False
            break

# 輸出結果
if is_geometric:
    print("Yes")
else:
    print("No")