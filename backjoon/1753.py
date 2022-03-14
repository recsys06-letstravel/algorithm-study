# https://www.acmicpc.net/problem/1753
# 최단경로

import sys
from queue import PriorityQueue

num_of_V, num_of_E = list(map(int, sys.stdin.readline().strip().split()))
start_V = int(sys.stdin.readline().strip())
graph = [[] for _ in range(num_of_V+1)]
distance = [float('inf')]*(num_of_V+1)
distance_priority = PriorityQueue()
visited = [False]*(num_of_V+1)

for _ in range(num_of_E):
    u, v, w = list(map(int, sys.stdin.readline().strip().split()))
    graph[u].append((v, w))

# 시작 노드에 대해서 초기화
distance[start_V] = 0
visited[start_V] = True
visited[0] = True


# 시작 노드에서 바로 다음으로 가는 노드들의 최단거리 저장
for next_v, next_w in graph[start_V]:
    if distance[next_v] > next_w : 
        distance[next_v] = next_w
        distance_priority.put((next_w, next_v))

# 시작 노드를 제외하고 반복
for i in range(num_of_V-1):
    # 현재 최단 거리가 가장 짧은 노드를 가져 온다
    # min_dis = float('inf')
    # min_idx = 0
    # for j in range(1, num_of_V+1):        
    #     if distance[j] < min_dis and not visited[j]:
    #         min_dis = distance[j]
    #         min_idx = j
    # visited[min_idx] = True
    if not distance_priority.empty() : 
        min_dis, min_idx = distance_priority.get()
        visited[min_idx] = True
    else : 
        min_idx = visited.index(False)
        min_dis = distance[min_idx]
        visited[min_idx] = True

    # 최단거리가 가장 짧은 노드의 다음 노드와 거리를 가져온다
    for next_v, next_w in graph[min_idx]:
        # 최단거리 변수에 있는 거리보다 현재 노드에서 다른 노드로 가는 거리가 짧은 경우
        if distance[min_idx] + next_w < distance[next_v]:
            distance[next_v] = distance[min_idx] + next_w

# 출력
for i in range(1, num_of_V+1):
    if distance[i] == float('INF') : print("INF")
    else : print(distance[i])


