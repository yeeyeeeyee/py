import sys
num_of_items = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

average = sum(num_list) / num_of_items
if average >= 183:
    print("real")
else:
    print("fake")
