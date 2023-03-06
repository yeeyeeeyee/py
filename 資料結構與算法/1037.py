import sys
target = int(sys.stdin.readline())
n = int(sys.stdin.readline())
result = []
for i in range(n):
    num = int(sys.stdin.readline())
    if num != target:
        result.append(num)

for num in result:
    print(num)