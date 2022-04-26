T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    day=int(input())
    List=list(map(int,input().strip().split()))
    
    
    answer=0
    while True:
        max_idx=List.index(max(List))
        if max_idx==0:
            List=List[1:]
            if len(List)==0:
                break
            else:
                continue
        else:
            answer+=max_idx*List[max_idx]-sum(List[:(max_idx)])
            List=List[(max_idx+1):]
            if len(List)==0:
                break
    print(f'#{test_case}',answer)
    # ///////////////////////////////////////////////////////////////////////////////////
