import sys
'''
Python3로 제출시 시간초과뜨므로
Pypy3로 제출할 것!
'''
INF=int(1e9)
# V,E=3,4
# Data=[[1,2,1],[3,2,1],[1,3,5],[2,3,2]]
V,E=map(int,sys.stdin.readline().split())
Data=[]
for i in range(E):
    Data.append(list(map(int,sys.stdin.readline().split())))
road=[[INF]*(V+1) for _ in range(V+1)]


for a,b,c in Data:
    road[a][b]=c
for a in range(V+1):
    for b in range(V+1):
        for c in range(V+1):
            road[b][c]=min(road[b][c],road[b][a]+road[a][c])
answer=INF
for a in range(1,V+1):
    if road[a][a]<answer:
        answer=road[a][a]
if answer==INF:
    print(-1)
else:
    print(answer)