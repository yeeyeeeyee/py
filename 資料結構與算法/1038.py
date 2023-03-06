import sys
target = int(sys.stdin.readline())
n = int(sys.stdin.readline())
found = False
for i in range(n):
    num = int(sys.stdin.readline())
    if num == target:
        print(i)
        found = True
        break

if not found:
    print(-1)