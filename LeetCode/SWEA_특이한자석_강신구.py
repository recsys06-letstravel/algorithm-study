from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    K=int(input().strip())
    M=[list(map(int,input().strip().split())) for _ in range(4)]    # N : 0, S : 1
    List=[list(map(int,input().strip().split())) for _ in range(K)]    # [자석번호, 방향] => 1 : 시계, -1 : 반시계
    answer=0
    def bfs(graph):
        queue=deque()
        queue.append(graph)
        memo=[]
        while queue:
            X,Y=queue.popleft()    # 좌석번호, 방향
            memo.append(X)
            # 좌
            if X-1>=0:
            	if M[X][6]!=M[X-1][2]:
                    if X-1 not in memo:
                    	queue.append([X-1,-1 if Y==1 else 1])
            if X+1<=3:
            	if M[X][2]!=M[X+1][6]:
                    if X+1 not in memo:
                    	queue.append([X+1,-1 if Y==1 else 1])
            if Y==1:
                M[X].insert(0,M[X].pop(-1))
            else:
                M[X].append(M[X].pop(0))
    for a in range(K):
        List[a][0]=List[a][0]-1
        bfs(List[a])
    if M[0][0]==1:
        answer+=1
    if M[1][0]==1:
        answer+=2
    if M[2][0]==1:
        answer+=4
    if M[3][0]==1:
        answer+=8
    print(f'#{test_case}',answer)
    # ///////////////////////////////////////////////////////////////////////////////////
