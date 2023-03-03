import sys
count=sys.stdin.readline().strip('\n')
name_and_value={}
value=[]
for i in range(int(count)):
    
    temp=sys.stdin.readline().strip('\n').split()
    name_and_value={temp[0]:temp[1]}
    value.append(int(temp[1]))
    
    
    print(f'{name_and_value} and {max(value)}') #測試



    