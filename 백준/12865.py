# 입력 처리
import sys
sys.stdin = open('testCase.txt', 'r')
n, k = map(int, input().split())  # 물건의 수 N, 배낭의 최대 무게 K
items = []  # (무게, 가치) 튜플로 저장

for _ in range(n):
    w, v = map(int, input().split())
    items.append((w, v))

# DP 배열 초기화
dp = [0] * (k + 1)

# 동적 프로그래밍으로 문제 해결
for w, v in items:
    for weight in range(k, w - 1, -1):  # 뒤에서부터 순회
        dp[weight] = max(dp[weight], dp[weight - w] + v)

# 결과 출력
print(dp[k])