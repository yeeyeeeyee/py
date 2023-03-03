import sys
# 第一次輸入
count = sys.stdin.readline().strip('\n')
#總文字長度
strlen=""
#增加程度
addlen=""
#把字串在一起
for i in range(int(count)):
    addlen=sys.stdin.readline().strip('\n')
    strlen+=addlen
    #print("output:"+str(i))
#print("test:"+strlen)
#答案長度
anslen=sys.stdin.readline().strip('\n')
#答案
ans=""
#位置
addition=""
#解答
for i in range(int(anslen)):
    addition=sys.stdin.readline().strip('\n')
    ans+=strlen[int(addition)-1]
#print("answer:"+ans)
print(ans)