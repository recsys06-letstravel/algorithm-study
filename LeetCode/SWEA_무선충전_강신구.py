T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    M,C=map(int,input().strip().split())    # M : 이동 횟수, C : 총 charger 갯수
    A_move=list(map(int,input().strip().split()))    # A가 움직인 정보
    B_move=list(map(int,input().strip().split()))    # B가 움직인 정보
    Charger=[list(map(int,input().strip().split())) for _ in range(C)]    # Charger의 위치(x, y), 거리, 충전량
    dx=[0,0,1,0,-1]    # 상, 우, 하, 좌
    dy=[0,-1,0,1,0]
    A_loc=[0,0]    # A의 시작지점(y,x)
    B_loc=[9,9]    # B의 시작지점(y,x)
    answer=0
    for a in range(M+1):
        # 이동
        if a!=0:
        	A_loc[1]=A_loc[1]+dx[A_move[a-1]]
        	A_loc[0]=A_loc[0]+dy[A_move[a-1]]
        	B_loc[1]=B_loc[1]+dx[B_move[a-1]]
        	B_loc[0]=B_loc[0]+dy[B_move[a-1]]
        A_list=[]
        B_list=[]
        for b in range(C):
            # 거리 측정해서 Charger 담기
            # A
            dist=abs(A_loc[0]-(Charger[b][1]-1))+abs(A_loc[1]-(Charger[b][0]-1))
            if dist<=Charger[b][2]:
                A_list.append(b)
            # B
            dist=abs(B_loc[0]-(Charger[b][1]-1))+abs(B_loc[1]-(Charger[b][0]-1))
            if dist<=Charger[b][2]:
                B_list.append(b)
        # 충전할 Charger 선택
        memo=[]
        if len(A_list)==0 and len(B_list)==0:
            answer+=0
        elif len(A_list)!=0 and len(B_list)==0:
            for c in range(len(A_list)):
                memo.append(Charger[A_list[c]][3])
            answer+=max(memo)
        elif len(A_list)==0 and len(B_list)!=0:
            for c in range(len(B_list)):
                memo.append(Charger[B_list[c]][3])
            answer+=max(memo)
        else:
            for c in range(len(A_list)):
                for d in range(len(B_list)):
                    if A_list[c]==B_list[d]:
                        memo.append(Charger[A_list[c]][3])
                    else:
                        memo.append(Charger[A_list[c]][3]+Charger[B_list[d]][3])
            answer+=max(memo)
    print(f'#{test_case}',answer)
    # ///////////////////////////////////////////////////////////////////////////////////
