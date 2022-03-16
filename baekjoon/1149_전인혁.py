import sys

n = int(sys.stdin.readline().strip())

houses = []

for i in range(n):
    r, g, b = map(int,sys.stdin.readline().strip().split())
    houses.append([r,g,b])

dp = []
for _ in range(3):
    line = []
    for _ in range(n):
        line.append(0)
    dp.append(line)

for index, house in enumerate(houses):
    if index == 0:
        dp[0][0] = house[0]
        dp[1][0] = house[1]
        dp[2][0] = house[2]

    dp[0][index] = house[0] + min(dp[1][index-1], dp[2][index-1])
    dp[1][index] = house[1] + min(dp[0][index-1], dp[2][index-1])
    dp[2][index] = house[2] + min(dp[0][index-1], dp[1][index-1])

print(min(dp[0][n-1], dp[1][n-1], dp[2][n-1]))