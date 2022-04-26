T=10

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for x in range(T):
    L=0
    R=0
    Big=0
    answer=0
    # ///////////////////////////////////////////////////////////////////////////////////
    number=int(input())
    List=list(map(int,input().strip().split(" ")))
    for i in range(number):
        if (i==0):
            continue
        elif (i==1):
            continue
        elif (i==number-1):
            continue
        elif (i==number-2):
            continue
        else:
            if List[i-2]>=List[i-1]:
                L=List[i-2]
            else:
                L=List[i-1]
            if List[i+1]>=List[i+2]:
                R=List[i+1]
            else:
                R=List[i+2]
            if L>=R:
                Big=L
            else:
                Big=R
            if List[i]>Big:
            	answer+=(List[i]-Big)
    #       answer+=(List[i]-max(max(List[i-1],List[i-2]),max(List[i+1],List[i+2])))
    print(f'#{x+1}',answer)
    # ///////////////////////////////////////////////////////////////////////////////////