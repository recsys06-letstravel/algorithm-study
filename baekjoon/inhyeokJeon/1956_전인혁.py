import sys
import heapq

V, E = map(int, sys.stdin.readline().strip().split(" "))
# K = int(sys.stdin.readline().strip())
INF = float('inf')
edges = []
graph = [[] for _ in range(V+1)]

hq = []

for _ in range(E):
    start, to, weight = map(int, sys.stdin.readline().strip().split(" "))
    graph[start].append((to,weight))

# heapq.heappush(heapq, (weight, vertex) )
# heapq.heappop(hq)

def dijkstra(start):
    # 메모리 초과 나는듯.
    distances = [INF for _ in range(V + 1)]
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

    return distances[1:]

shortestPath = []
for i in range(1,V+1):
    shortestPath.append(dijkstra(i))

minimum = INF
for i in range(V):
    for j in range(i+1,V):
        if shortestPath[i][j] != INF and shortestPath[j][i] != INF:
            minimum = min(minimum, shortestPath[i][j] + shortestPath[j][i])

# print(shortestPath)
if minimum == INF:
    print(-1)
else:
    print(minimum)

