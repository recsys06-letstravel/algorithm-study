from collections import deque
from itertools import product
import copy

def Break(graph,w,h):
    queue=deque()
    queue.append((w,h,graph[w][h]))
    while queue:
        Y, X,number=queue.popleft()
        graph[Y][X]=0
        dx=[0]*(number-1)+[0]*(number-1)+[i for i in range(-(number-1),0)]+[i for i in range(1,number)]
        dy=[i for i in range(-(number-1),0)]+[i for i in range(1,number)]+[0]*(number-1)+[0]*(number-1)
        for i in range(len(dx)):
            nx=X+dx[i]
            ny=Y+dy[i]
            if nx<=-1 or nx>=W or ny<=-1 or ny>=H:
                continue
            elif graph[ny][nx]==0:
                continue
            else:
                queue.append((ny,nx,graph[ny][nx]))
                graph[ny][nx]=0
    return graph

def re_change(graph):
    graph=[list(k) for k in tuple(zip(*graph))]
    for i in graph:
        for j in range(len(i)):
            if i[j]==0:
                i.pop(j)
                i.insert(0,0)
    graph=[list(k) for k in tuple(zip(*graph))]
    return graph

T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N,W,H=map(int, input().strip().split())
    List=[]
    for i in range(H):
        List.append(list(map(int,input().strip().split())))
    answer=[]
    flag=0
    Location=deque(product([i for i in range(W)], repeat=N))
    for a in Location:
        memo=copy.deepcopy(List)
        count=0
        hap=0
        for b in a:
            List1=[list(k) for k in tuple(zip(*memo))][b]
            n=-1
            y_loc=0
            for c in List1:
                n+=1
                if c>0:
                    y_loc=n
                    break
            if (n==len(List1)) and (y_loc==0):
                break
            memo=Break(memo,y_loc,b)
            memo=re_change(memo)
            for f in memo:
                hap+=sum(f)
            if hap==0:
                flag=1
                break
        if flag==1:
            answer.append(0)
            break
        for d in range(H):
            for e in range(W):
                if memo[d][e]>0:
                    count+=1
        answer.append(count)
    answer=min(answer)
    print(f'#{test_case}',answer)
    # ///////////////////////////////////////////////////////////////////////////////////
