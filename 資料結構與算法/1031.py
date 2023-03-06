import sys
def sum_of_squares(n: int) -> int:
    # 初始化總和
    total = 0
    
    # 計算完全平方數的總和
    for i in range(1, n + 1):
        if (i ** 0.5).is_integer():
            total += i
    
    return total

# 測試範例
print(sum_of_squares(int(sys.stdin.readline()))) # 輸出 55