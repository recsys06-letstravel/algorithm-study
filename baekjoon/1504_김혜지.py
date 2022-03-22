# https://www.acmicpc.net/problem/1504
# 특정한 최단 경로
import sys
from queue import PriorityQueue

def get_dist(node1, node2):
    distance = [float("inf")]*(num_of_V+1)
    priority_Q = PriorityQueue()

    distance[node1] = 0
    priority_Q.put((0, node1))

    while not priority_Q.empty():
        current_dis, current_node = priority_Q.get()

        if distance[current_node] < current_dis: continue

        for next_node, next_dis in graph[current_node]:
            if distance[current_node]+next_dis < distance[next_node]:
                distance[next_node] = distance[current_node]+next_dis
                priority_Q.put((distance[next_node], next_node))

    return distance[node2]


num_of_V, num_of_E = list(map(int, sys.stdin.readline().strip().split()))
graph = [[] for _ in range(num_of_V+1)]


for _ in range(num_of_E):
    node1, node2, dis = list(map(int, sys.stdin.readline().strip().split()))
    graph[node1].append((node2, dis))
    graph[node2].append((node1, dis))

mid_node1, mid_node2 = list(map(int, sys.stdin.readline().strip().split()))

results = [get_dist(1, mid_node1)+get_dist(mid_node1, mid_node2)+get_dist(mid_node2, num_of_V), \
            get_dist(1, mid_node2)+get_dist(mid_node2, mid_node1)+get_dist(mid_node1, num_of_V)]

if min(results) == float("inf") : print(-1)
else : print(min(results))







