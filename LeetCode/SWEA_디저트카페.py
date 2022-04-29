T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N=int(input().strip())
    List=[list(map(int,input().strip().split())) for i in range(N)]
    
    # 사각형의 길이
    box=[]
    for a in range(1,N-1):
        for b in range(1,N-1):
            if a+b<=N-1:
            	box.append([a,b])
            
    def hamsu(graph,y,x):
        L=[]
        for e in box:
            flag=0
            dl,dr=e[0],e[1]
            if (x-dl<0) or (x+dr>N-1) or (y+e[0]+e[1]>N-1):
                continue
            else:
                memo=[]
                for f in range(e[1]):
                    #print('1',graph[y+f+1][x+f+1])
                    if graph[y+f+1][x+f+1] in memo:
                        flag=1
                        break
                    else:
                    	memo.append(graph[y+f+1][x+f+1])
                for g in range(e[0]):
                    #print('2',graph[y+f+1+g+1][x+f+1-g-1])
                    if flag==1:
                        break
                    if graph[y+f+1+g+1][x+f+1-g-1] in memo:
                        flag=1
                        break
                    else:
                    	memo.append(graph[y+f+1+g+1][x+f+1-g-1])
                for h in range(e[1]):
                    #print('3',graph[y+f+1+g+1-h-1][x+f+1-g-1-h-1])
                    if flag==1:
                        break
                    if graph[y+f+1+g+1-h-1][x+f+1-g-1-h-1] in memo:
                        flag=1
                        break
                    else:
                    	memo.append(graph[y+f+1+g+1-h-1][x+f+1-g-1-h-1])
                for i in range(e[0]):
                    #print('4',graph[y+f+1+g+1-h-1-i-1][x+f+1-g-1-h-1+i+1])
                    if flag==1:
                        break
                    if graph[y+f+1+g+1-h-1-i-1][x+f+1-g-1-h-1+i+1] in memo:
                        flag=1
                        break
                    else:
                    	memo.append(graph[y+f+1+g+1-h-1-i-1][x+f+1-g-1-h-1+i+1])
                #print(memo)
                if flag==1:
                    continue
                else:
                    L.append(len(memo))
        if L==[]:
            L=0
        else:
            L=max(L)
        return L
    answer=[]
    for c in range(N):
        for d in range(N):
            if (c==0 and d==0) or (c==0 and d==N-1) or (c==N-1 and d==0) or (c==N-1 and d==N-1):
                continue
            else:
                answer.append(hamsu(List,c,d))
                #print(answer)
    if max(answer)==0:
        print(f'#{test_case}',-1)
    else:
        print(f'#{test_case}',max(answer))
    # ///////////////////////////////////////////////////////////////////////////////////
