import sys
import heapq

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

bus_list = []
graph = [[] for _ in range(N+1)]


# print(graph)
for _ in range(M):
    start, end, weight = map(int, sys.stdin.readline().strip().split(" "))
    graph[start].append((end, weight))

def dijkstra(start):
    distances = [10000000001 for _ in range(N + 1)]
    distances[start] = 0
    hq = []
    heapq.heappush(hq, (0, start))
    while hq:
        cost, here = heapq.heappop(hq)
        if distances[here] < cost:
            continue
        for there, there_cost in graph[here]:
            next_dist = there_cost + cost
            if distances[there] > next_dist:
                distances[there] = next_dist
                heapq.heappush(hq, (next_dist,there))
    return distances[1:N+1]

for _ in range(1,N+1):
    for kk in dijkstra(_):
        if kk > 10000000000:
            print(0, end=" ")
        else:
            print(kk, end=" ")
    print()

