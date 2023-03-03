import sys
# 定義一個函數來計算方法數
def count_ways(n):
  # 如果目標樓層小於等於零，則沒有方法
  if n <= 0:
    return 0
  # 如果目標樓層等於一或二，則只有一種方法
  elif n == 1 or n == 2:
    return 1
  # 否則，使用遞迴方式計算方法數
  else:
    return count_ways(n - 1) + count_ways(n - 2)

# 詢問使用者想要到達的目標樓層
target = int(sys.stdin.readline())

# 呼叫函數並印出結果
result = count_ways(target)
print(result)