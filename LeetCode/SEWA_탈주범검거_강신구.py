from collections import deque
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N,M,R,C,Time=map(int,input().strip().split())
    List=[list(map(int,input().strip().split())) for i in range(N)]
    Tunnel=[[0,1,2,3],[0,1],[2,3],[0,3],[1,3],[1,2],[0,2]]
    
    def check_out(dir,Next):
        if Next==0:
            return False
        if dir==0:
            if Next==3 or Next==4 or Next==7:
                return False
            else:
                return True 
        elif dir==1:
            if Next==3 or Next==5 or Next==6:
                return False
            else:
                return True
        elif dir==2:
            if Next==2 or Next==6 or Next==7:
                return False
            else:
                return True
        else:
            if Next==2 or Next==4 or Next==5:
                return False
            else:
                return True
            
    def bfs(y,x):
        memo=[]
        if List[y][x]==0:
            return False
        queue=deque()
        memo.append([y,x])
        queue.append([List[y][x],y,x])
        number=1
        count=1
        dx=[0,0,-1,1]
        dy=[-1,1,0,0]    # 상, 하, 좌, 우
        while queue:
            for b in range(len(queue)):
                T_type,Y,X=queue.popleft()
                for a in Tunnel[T_type-1]:
                    nx=X+dx[a]
                    ny=Y+dy[a]
                    if nx<0 or ny<0 or nx>M-1 or ny>N-1:
                        continue
                    else:
                        if check_out(a,List[ny][nx]):
                            if [ny,nx] not in memo:
                                queue.append([List[ny][nx],ny,nx])
                                memo.append([ny,nx])
                                number+=1
                        else:
                            continue
            count+=1
            if count==Time:
                break
        return number
    answer=bfs(R,C)
    if Time==1:
        print(f'#{test_case}',1)
    else:
        print(f'#{test_case}',answer)
    # ///////////////////////////////////////////////////////////////////////////////////
