# https://www.acmicpc.net/problem/1956
# 운동

import sys

num_of_V, num_of_E = list(map(int, sys.stdin.readline().strip().split()))
graph =[[float("inf")]*(num_of_V+1) for _ in range(num_of_V+1)]

# 간선의 정보를 입력받음
for _ in range(num_of_E):
    node1, node2, dis = list(map(int, sys.stdin.readline().strip().split()))
    graph[node1][node2] = dis

# 점화식을 통해 플로이드 워셜 알고리즘 수행
for i in range(1, num_of_V+1):
    for j in range(1, num_of_V+1):
        for k in range(1, num_of_V+1):
            graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])

# 자기 자신으로 돌아오는 싸이클을 구한다
cycle_result = float("inf")
for i in range(1, num_of_V+1):
    cycle_result = min(cycle_result, graph[i][i])

# 출력
if cycle_result == float("inf") : print(-1)
else : print(cycle_result)