import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

max_length = 0
current_length = 1

for i in range(1, n):
    if a[i] == a[i-1]:
        current_length += 1
    else:
        max_length = max(max_length, current_length)
        current_length = 1

max_length = max(max_length, current_length)

print(max_length)