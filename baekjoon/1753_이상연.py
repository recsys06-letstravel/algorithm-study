import heapq
import sys
input=sys.stdin.readline

V, E = map(int, input().split())
k = int(input())
graph=[[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u].append([v,w])
inf = int(1e9)
distance = [inf]*(V+1)
q=[]

distance[k] = 0

heapq.heappush(q, (0,k))
while q:
    dis,now = heapq.heappop(q)
    if distance[now] < dis:
        continue
    for i in graph[now]:
        if dis + i[1] < distance[i[0]]:
            distance[i[0]] = dis+i[1]
            heapq.heappush(q, (dis+i[1],i[0]))
            
for i in range(1,V+1):
    print('INF' if distance[i]==inf else distance[i])