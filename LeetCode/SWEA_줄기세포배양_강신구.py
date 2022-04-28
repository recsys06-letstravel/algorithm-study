T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    H,W,Time=map(int, input().strip().split())
    List=[]
    for i in range(H):
        List.append(list(map(int,input().strip().split())))
    answer=0
    Slice=[[i*0 for i in range(352)] for _ in range(352)]
    for i in range(H):
        for j in range(W):
            if List[i][j]!=0:
                Slice[(352-H)//2+i][(352-W)//2+j]=[List[i][j],List[i][j]]
    for a in range(Time):
        for b in range((352-H)//2-a//2-1,352-((352-H)//2-a//2-1)+1):
            for c in range((352-W)//2-a//2-1,352-((352-W)//2-a//2-1)+1):
                memo=[]
                if Slice[b][c]==0:
                    if b+1<352:
                        if Slice[b+1][c]!=0:
                            if Slice[b+1][c][1]==0:
                                memo.append(Slice[b+1][c][0])
                    if b-1>-1:
                        if Slice[b-1][c]!=0:
                            if Slice[b-1][c][1]==0:
                                memo.append(Slice[b-1][c][0])
                    if c+1<352:
                        if Slice[b][c+1]!=0:
                            if Slice[b][c+1][1]==0:
                                memo.append(Slice[b][c+1][0])
                    if c-1>-1:
                        if Slice[b][c-1]!=0:
                            if Slice[b][c-1][1]==0:
                                memo.append(Slice[b][c-1][0])
                    if len(memo)==0:
                        continue
                    else:
                        Slice[b][c]=[max(memo),max(memo)+1]
        for b in range((352-H)//2-a//2-1,352-((352-H)//2-a//2-1)+1):
            for c in range((352-W)//2-a//2-1,352-((352-W)//2-a//2-1)+1):
                if Slice[b][c]!=0:
                    if Slice[b][c]!=-1:
                    	if Slice[b][c][0]==-(Slice[b][c][1]-1):
                        	Slice[b][c]=-1
                    	else:
                            Slice[b][c][1]-=1
                    else:
                        continue
    for a in range(352):
        for b in range(352):
            if Slice[a][b]!=0 and Slice[a][b]!=-1:
                answer+=1
    print(f'#{test_case}',answer)
    # ///////////////////////////////////////////////////////////////////////////////////
