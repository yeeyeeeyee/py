from collections import deque
import sys
def bfs(maze, w, h):
    # 定義四個方向
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # 創建一個佇列，並將起點加入佇列中
    queue = deque([(0, 0)])
    # 記錄從起點到每個位置的步數
    steps = [[0] * w for _ in range(h)]
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and maze[nx][ny] == '.':
                # 如果該位置沒有被訪問過，則加入佇列中
                if steps[nx][ny] == 0:
                    steps[nx][ny] = steps[x][y] + 1
                    queue.append((nx, ny))
    
    return steps[h-1][w-1]

w,h=map(int,sys.stdin.readline().split())
maze=[]
for i in range(h):
    maze.append(list(sys.stdin.readline()))
print(bfs(maze,w,h))