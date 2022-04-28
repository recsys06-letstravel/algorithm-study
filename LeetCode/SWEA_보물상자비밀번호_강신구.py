T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, K=map(int,input().strip().split())
    List=list(input().strip().split()[0])
    answer=[]
    Dict={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    for i in range(N//4):
        for j in range(4):
            memo=0
            for k in range(N//4):
                memo+=(16**(N//4-1-k))*Dict[List[j*(N//4)+k]]
            if memo not in answer:
            	answer.append(memo)
        List.insert(0,List.pop(-1))
    answer=sorted(answer,reverse=True)
    answer=answer[K-1]
    print(f'#{test_case}',answer)
    # ///////////////////////////////////////////////////////////////////////////////////
