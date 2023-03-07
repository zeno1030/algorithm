N = int(input())
p = [0] + list(map(int, input().split()))
dp = [9999999 for _ in range(N+1)]
dp[0] = 0

for i in range(1, N+1):
    for k in range(1, i+1):
        dp[i] = min(dp[i], dp[i-k] + p[k])


print(dp[N])
