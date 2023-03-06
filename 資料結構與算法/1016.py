import sys
N = int(sys.stdin.readline())
A_count = 0
B_count = 0
a_list = []
b_list = []
for i in range(1,N+1):
    answer = sys.stdin.readline().strip()
    if answer == "A":
        A_count += 1
        a_list.append(i)
    else:
        B_count += 1
        b_list.append(i)

if A_count==0 or B_count==0 or A_count == B_count:
    print('PEACE')
else:
    if A_count>B_count:
        for i in b_list:
            print(i)
        
    else:
        for i in a_list:
            print(i)

   