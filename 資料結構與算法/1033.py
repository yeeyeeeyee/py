import sys
import math

n = int(sys.stdin.readline())
points = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x,y))

min_distance = float('inf')
result = []
for i in range(n):
    for j in range(i+1,n):
        p1 = points[i]
        p2 = points[j]
        distance = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
        if distance < min_distance:
            min_distance = distance
            result = [p1,p2]

result.sort(key=lambda x: (x[0],x[1]))
print(result[0][0], result[0][1])
print(result[1][0], result[1][1])