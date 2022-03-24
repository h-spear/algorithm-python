# https://www.acmicpc.net/problem/15992

dp = [[0] * 1001 for _ in range(1001)]
dp[1][1] = 1
dp[2][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 2
dp[3][3] = 1
p = 1000000009

for i in range(4, 1001):
    for j in range(2, 1001):
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 2][j - 1] + dp[i - 3][j - 1]) % p

for tc in range(int(input())):
    n, m = map(int, input().split())
    print(dp[n][m])
