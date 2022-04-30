import copy
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N,Time,K=map(int,input().strip().split())    # N : 사각형 길이, Time : 시간, K : 군집의 수
    List=[list(map(int,input().strip().split())) for i in range(K)]    # [세로, 가로, 미생물 수, 이동방향]
    Map=[[0 for i in range(N)] for j in range(N)]
    dx=[0,0,-1,1]    # 상: 1, 하: 2, 좌: 3, 우: 4
    dy=[-1,1,0,0]
    for a in range(Time):
        num=0
        for b in range(len(List)):
            b=b-num
            List[b][0]=List[b][0]+dy[List[b][3]-1]
            List[b][1]=List[b][1]+dx[List[b][3]-1]
            if (List[b][0]==0) or (List[b][0]==(N-1)) or (List[b][1]==0) or (List[b][1]==(N-1)):
                List[b][2]=List[b][2]//2
                if List[b][2]==0:
                    List.pop(b)
                    num+=1
                    continue
                if List[b][3]==1:
                    List[b][3]=2
                elif List[b][3]==2:
                    List[b][3]=1
                elif List[b][3]==3:
                    List[b][3]=4
                elif List[b][3]==4:
                    List[b][3]=3
        while True:
            A=len(List)-1
            for c in range(A):
                flag=0
                memo=[]
                hap=0
                way=[]
                locate=copy.deepcopy([List[c][0],List[c][1]])
                for d in range(c+1,len(List)):
                    if (List[c][0]==List[d][0]) and (List[c][1]==List[d][1]):
                        memo.append(d)
                        way.append([List[d][2],List[d][3]])
                if memo!=[]:
                    memo.append(c)
                    way.append([List[c][2],List[c][3]])
                    memo=sorted(memo,reverse=True)
                    way=sorted(way,reverse=True)
                    for e in range(len(memo)):
                        hap+=List[memo[e]][2]
                    List.append(locate+[hap]+[way[0][1]])
                    for f in memo:
                        List.pop(f)                        
                    flag=1      
                else:
                    continue
                if flag==1:
                    flag=0
                    break
            if c==A-1:
                break
        
    answer=0
    for f in range(len(List)):
        answer+=List[f][2]
    print(f'#{test_case}',answer)
    # ///////////////////////////////////////////////////////////////////////////////////
