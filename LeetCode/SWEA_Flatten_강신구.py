T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    number = int(input())
    List=list(map(int,input().strip().split(" ")))
    for i in range(number):
        if max(List)-min(List)<=1:
            answer=List[high_idx]-List[low_idx]
            break
        else:
            high_idx=List.index(max(List))
            low_idx=List.index(min(List))
            List[high_idx]=List[high_idx]-1
            List[low_idx]=List[low_idx]+1
            answer=max(List)-min(List)
    print(f'#{test_case}',answer)
    # ///////////////////////////////////////////////////////////////////////////////////
