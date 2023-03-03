
import sys

def whoisbigger(A,B):
  print(tmp)
  if int(A)==int(B):
    return(int(A))
  elif int(A)>int(B):
    return int(A)
  else:
    return int(B)

ans=[]

# 第一次輸入
str = sys.stdin.readline().strip('\n')
tmp = str.split()

# 先判斷有沒有第二次輸入
while int(tmp[0])!=0 or int(tmp[1])!=0:
  
  #計算上一次的比大小結果 
  ans.append(whoisbigger(tmp[0],tmp[1]))
  
  #輸入下一行的A 和 B，直到A=B=0
  str = sys.stdin.readline().strip('\n')
  tmp = str.split() 


#   印出比大小結果，一行一行印
for everyans in ans:
  print(everyans)