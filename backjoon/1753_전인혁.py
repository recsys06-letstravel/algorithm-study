import sys
import heapq

V, E = map(int, sys.stdin.readline().strip().split(" "))
K = int(sys.stdin.readline().strip())

edges = []
graph = [[] for _ in range(V+1)]
distances = [200001 for _ in range(V+1)]
hq = []

for _ in range(E):
    start, to, weight = map(int, sys.stdin.readline().strip().split(" "))
    graph[start].append((to,weight))

# heapq.heappush(heapq, (weight, vertex) )
# heapq.heappop(hq)
def dijkstra(start):
    # 메모리 초과 나는듯.
    distances[start] = 0
    heapq.heappush(hq, (0, start)) # 0 weight 0 vertex
    while hq:
        cost, here = heapq.heappop(hq)
        if distances[here] < cost:
            continue
        for there, there_dist in graph[here]:
            next_dist = cost + there_dist
            if distances[there] > next_dist:
                distances[there] = next_dist
                heapq.heappush(hq, (next_dist, there))

    return distances

for index, i in enumerate(dijkstra(K)):
    if index == 0 :
        continue
    if i > 200000:
        print("INF")
    else:
        print(i)






