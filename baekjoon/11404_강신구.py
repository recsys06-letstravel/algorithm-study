import sys

INF=int(1e9)

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
# n+1 X n+1 크기의 데이터 만들기 /[0]라인은 무시/
data=[[INF]*(n+1) for _ in range(n+1)]


# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for x in range(1,n+1):
    data[x][x]=0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    a, b, c=map(int,sys.stdin.readline().split())
    if data[a][b]>c:
        data[a][b]=c



for x in range(1,n+1):
    for y in range(1,n+1):
        for z in range(1,n+1):
            data[y][z]=min(data[y][z],data[y][x]+data[x][z])



for x in range(1,n+1):
    for y in range(1,n+1):
        if y==n:
            if data[x][y]==INF:
                print(0)
            else:
                print(data[x][y])
        else: 
            if data[x][y]==INF:
                print(0, end=" ")
            else:
                print(data[x][y], end=" ")
