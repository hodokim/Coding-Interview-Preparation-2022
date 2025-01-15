import sys
import heapq

input = sys.stdin.readline

# 최소 힙을 저장할 리스트
min_heap = []

# 입력
N = int(input().strip())
for _ in range(N):
    x = int(input().strip())
    if x == 0:
        # 힙이 비어있으면 0 출력
        if not min_heap:
            print(0)
        else:
            # 힙에서 가장 작은 값을 꺼내고 출력
            print(heapq.heappop(min_heap))
    else:
        # 힙에 값을 추가
        heapq.heappush(min_heap, x)

#힙을 직접 구현해서 풀어보기