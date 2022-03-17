# https://www.acmicpc.net/problem/1753
# 최단경로

import sys
from queue import PriorityQueue


num_of_V, num_of_E = list(map(int, sys.stdin.readline().strip().split()))
start_V = int(sys.stdin.readline().strip())
graph = [[] for _ in range(num_of_V+1)]
distance = [float('inf')]*(num_of_V+1)
priority_Q = PriorityQueue()

distance[start_V] = 0
priority_Q.put((0, start_V))


for _ in range(num_of_E):
    u, v, w = list(map(int, sys.stdin.readline().strip().split()))
    graph[u].append((v, w))

while not priority_Q.empty():
    dist, current_node = priority_Q.get()
    # 이미 저장된 거리가 입력받은 거리보다 작으면 continue
    if distance[current_node] < dist:
        continue

    for next_node, next_dis in graph[current_node]:
        if distance[current_node] + next_dis < distance[next_node]:
            distance[next_node] = distance[current_node] + next_dis
            priority_Q.put((distance[current_node] + next_dis, next_node))
# 출력
for i in range(1, num_of_V+1):
    if distance[i] == float('INF') : print("INF")
    else : print(distance[i])

