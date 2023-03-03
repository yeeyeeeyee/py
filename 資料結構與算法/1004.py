import sys
def 判斷(A,B,judge):
    if judge==1:
        if A>B:
            return "A"
        elif A==B:
            return "DRAW"
        else:
            return "B"
    else:
        if A>B:
            return "B"
        elif A==B:
            return "DRAW"
        else:
            return "A"

count = sys.stdin.readline().strip('\n')

for i in range(int(count)):
    str=sys.stdin.readline().strip('\n')
    temp=str.split()
    print(判斷(int(temp[0]),int(temp[1]),int(temp[2])))
