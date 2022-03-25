import sys
import heapq

V, E = map(int, sys.stdin.readline().strip().split(" "))

INF = float('inf')
edges = []
graph = [[] for _ in range(V+1)]

hq = []

for _ in range(E):
    start, to, weight = map(int, sys.stdin.readline().strip().split(" "))
    graph[start].append((to,weight))
    graph[to].append((start, weight))


v1, v2 = map(int, sys.stdin.readline().strip().split(" "))

# heapq.heappush(heapq, (weight, vertex) )
# heapq.heappop(hq)

def dijkstra(start):
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

# min(1 to v1, v1 to v2, v2 to N , 1 to v2, v2, to v1, v1 to N)
minimum_path = min(dijkstra(1)[v1-1] + dijkstra(v1)[v2-1] + dijkstra(v2)[V-1], dijkstra(1)[v2-1] + dijkstra(v2)[v1-1] + dijkstra(v1)[V-1])

if minimum_path >= INF:
    print(-1)
else:
    print(minimum_path)

