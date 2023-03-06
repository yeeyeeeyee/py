import sys
N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
occupied = set()
for _ in range(M):
    occupied.add(int(sys.stdin.readline().strip()))

count = 0
for i in range(1, N+1):
    if i not in occupied:
        if i+1 <= N and (i+1) not in occupied:
            count += 1
        if i%2 == 1 and i+2 <= N and (i+2) not in occupied:
            count += 1

print(count)