T = int(input())

def f(n):
    if n == 0 :
        return 1
    if n == 1 :
        return 1
    else:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n +1):
            dp[i] = dp[i -1] + dp[i -2]

        return dp[n]

for _ in range(T):
    n = int(input())
    print(f(n))
