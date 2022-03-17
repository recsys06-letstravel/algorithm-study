# https://www.acmicpc.net/problem/11404
# 플로이드
import sys

num_of_node = int(sys.stdin.readline().strip())
num_of_edge = int(sys.stdin.readline().strip())

# 2차원 리스트로 그래프를 표현하고, 무한으로 초기화
graph = [[float('inf')]*(num_of_node+1) for _ in range(num_of_node+1)]

# 자기 자신은 0으로 처리
for i in range(1, num_of_node+1):
    for j in range(1, num_of_node+1):
        if i==j : graph[i][j] = 0

# 간선의 정보를 입력받음
for _ in range(num_of_edge):
    node1, node2, dis = list(map(int, sys.stdin.readline().strip().split()))
    if graph[node1][node2] > dis:
        graph[node1][node2] = dis

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for i in range(1, num_of_node+1):
    for j in range(1, num_of_node+1):
        for k in range(1, num_of_node+1):
            graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])

for i in range(1, num_of_node+1):
    for j in range(1, num_of_node+1):
        if graph[i][j] == float('INF') : print(0, end=" ")
        else : print(graph[i][j], end=" ")
    print()