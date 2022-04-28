import copy
    
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, X=map(int,input().strip().split())
    List=[list(map(int,input().strip().split())) for _ in range(N)]
    answer=0

    def check_out(graph):
        if len(graph)==1:
            return True
        flag1=0                                 # count를 이어가게 해주는 flag1
        flag2=0                                 # 최종 True를 내줄 flag2
        count=0
        for a in range(len(graph)):
            if len(set(graph))==1:              # 한 종류의 숫자로 이루어져 있으면 True
                return True
            if a==len(graph)-1:                 # Test_case 10번의 8, 9번 째 줄을 고려한 것
                if count<X:                     # 밑에서 X만큼 빼줬는데도 X보다 크면 반대로 만들 수 있다는 것을 고려
                    return False                
                else:
                    continue
            if graph[a]<graph[a+1]:             # Test_case 10번의 8, 9번 째 줄을 고려한 것
                if count>=2*X:                  # 작아졌다 커지니까 답을 포함하면 안될거 같지만 
                    count-=X                    # 높이가 3인 부분에 양쪽으로 3,3인 활주로를 만들 수 있으므로 포함시켜봄
                    flag2=1
                else:
                    return False
            elif graph[a]==graph[a+1]:          # 서로 같고 
                if flag1==1:                    # flag1이 1이라면 count를 세어줌
                    count+=1
                    if count==X:                # count가 X를 넘어가면 flag2=1로 만들어줌
                        flag2=1
                else:
                    continue                    # 만약 max로 뽑은 수과 같다면 넘어가기
            else:
                if graph[a]-graph[a+1]>1:       # 만약 높이 차이가 2이상이라면 False
                    return False
                else:
                    if count==0 or count>=X:    
                        count=0
                        count+=1
                        flag1=1
                    else:
                        return False            # 만약 count가 X보다 작은데 더 아래로 내려간다면 False
        if flag2==1:
            return True
    
    # line 한 줄씩 불러와 chech_out 해보기
    for i in range(N):
        if len(set(List[i]))==1:
            answer+=1
            continue
        else:
            Max=max(List[i])
            index=List[i].index(Max)
            #print(List[i][index:])
            #print(List[i][:(index+1)][::-1])
            #print(check_out(List[i][index:]))
            #print(check_out(List[i][:(index+1)][::-1]))
            if check_out(List[i][index:]) and check_out(List[i][:(index+1)][::-1]):    # 제일 높은 지점을 찾아 그 점을 포함하여 양쪽으로 check_out해보기
                answer+=1
                
    List=[list(i) for i in tuple(zip(*List))]    # 역행렬 만들어주기

    # line 한 줄씩 불러와 check_out 해보기
    for i in range(N):
        if len(set(List[i]))==1:
            answer+=1
            continue
        else:
            Max=max(List[i])
            index=List[i].index(Max)
            #print(List[i][index:])
            #print(List[i][:(index+1)][::-1])
            #print(check_out(List[i][index:]))
            #print(check_out(List[i][:(index+1)][::-1]))
            if check_out(List[i][index:]) and check_out(List[i][:(index+1)][::-1]):
                answer+=1
    print(f'#{test_case}',answer)
    # ///////////////////////////////////////////////////////////////////////////////////
