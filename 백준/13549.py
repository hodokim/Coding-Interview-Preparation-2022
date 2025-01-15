from collections import deque

def find_brother(N, K):
    MAX_POSITION = 100000
    visited = [False] * (MAX_POSITION + 1)

    # BFS 큐 초기화
    queue = deque([(N, 0)])  # (현재 위치, 시간)
    visited[N] = True

    while queue:
        current_position, time = queue.popleft()

        # 동생을 찾은 경우
        if current_position == K:
            return time

        # 가능한 다음 위치 (순간이동을 우선 처리)
        next_positions = [current_position * 2, current_position - 1, current_position + 1]
        for next_position in next_positions:
            if 0 <= next_position <= MAX_POSITION and not visited[next_position]:
                visited[next_position] = True
                # 순간이동은 동일 시간으로 처리
                if next_position == current_position * 2:
                    queue.appendleft((next_position, time))  # 우선 탐색
                else:
                    queue.append((next_position, time + 1))

# 입력 처리
import sys
sys.stdin = open('testCase.txt', 'r')
N, K = map(int, input().split())
print(find_brother(N, K))