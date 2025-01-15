import sys
sys.stdin = open('testCase.txt', 'r')
input = sys.stdin.readline

n = int(input())
dp = [0] * n
arr = list(map(int,input().split()))
dp[0] = arr[0]

for i in range(1, n):
    dp[i] = max(arr[i], dp[i-1]+arr[i])

print(max(dp))