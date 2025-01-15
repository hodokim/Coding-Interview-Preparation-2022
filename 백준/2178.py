from collections import deque

import sys
sys.stdin = open('testCase.txt', 'r')
input = sys.stdin.readline

def solution(n, m, grid):
    def can_move(x, y):
        return 0 <= x < n and 0 <= y < m

    queue = deque([(0,0,1)])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    while queue:
        x, y, dist = queue.popleft()

        if x == n-1 and y == m-1:
            return dist
        
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if can_move(nx,ny) and grid[nx][ny] == '1' and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny,dist+1))
    return -1


# 입력 처리
n, m = map(int, input().split())
grid = [input() for _ in range(n)]

print(solution(n,m,grid))