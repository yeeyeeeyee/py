import sys
# 讀取輸入
str = sys.stdin.readline()
n = int(sys.stdin.readline())

# 創建一個空列表來存儲數列中的元素
result = []
for i in range(n):
    num = sys.stdin.readline()
    result.append(num)

# 使用 join 方法將數列中的元素與 str 組合起來
output = str.join(result)
print(result)