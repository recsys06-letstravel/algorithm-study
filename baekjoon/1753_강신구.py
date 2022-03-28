import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
data=[[] for i in range(V+1)]
answer=[1e9]*(V+1)
'''
for i in range(E):
    u,v,w=map(int,sys.stdin.readline().split())
    data.append([u,v,w])
'''
'''
V,E=5, 6
K=1
data=[[5, 1, 1],[1, 2, 2],[1, 3, 3],[2, 3, 4],[2, 4, 5],[3, 4, 6]]

'''

for _ in range(E):
    u, v, w=map(int,sys.stdin.readline().split())
    data[u].append((v,w))
'''
print('V: ', V)
print('E: ', E)
print('data: ', data)
print('distance: ',answer)
'''

def dijkstra(start):
    q=[]
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q,(0,K))
    answer[K]=0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist,now=heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if answer[now]<dist:
            continue
        for i in data[now]:
            cost=dist+i[1]
            if cost<answer[i[0]]:
                answer[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(K)

for i in range(1,V+1):
    if answer[i]==1e9:
        print('INF')
    else:
        print(answer[i])
