# https://www.acmicpc.net/problem/1149
# RGB 거리
import sys

n = int(sys.stdin.readline().strip())
house = list()
cost_sum_list = list()

dp = [[]]

for _ in range(n):
    r, g, b = map(int, sys.stdin.readline().strip().split(" "))
    house.append([r, g, b])

dp[0] = house[0]

for i in range(1, n):
    dp.append([])
    dp[i] = [min(house[i][0]+dp[i-1][1], house[i][0]+dp[i-1][2]), \
            min(house[i][1]+dp[i-1][0], house[i][1]+dp[i-1][2]), \
            min(house[i][2]+dp[i-1][0], house[i][2]+dp[i-1][1])]

print(min(dp[-1]))