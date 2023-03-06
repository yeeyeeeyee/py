# 輸入N和M
import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

# 雙重循環遍歷每一個數字
for i in range(1, N+1):
    for j in range(1, M+1):
        ans=i*j
        # 計算乘積並輸出
        print(str(i)+"*"+str(j)+"="+str(ans))