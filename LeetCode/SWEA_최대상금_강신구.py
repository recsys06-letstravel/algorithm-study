T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    number, count=map(int, input().strip().split())
    number=list(str(number))
    high=sorted(number,reverse=True)
    for i in range(count):
        flag=0
        if high==number:
            if len(number)!=len(set(number)):
                continue
            else:
                number.insert(-1,number.pop(len(number)-1))
        else:
            for j in range(len(number)-1):
                num_idx=[]
                high_num=[]
                index=0
                index_count=0
                if number[j]==high[j]:
                    continue
                else:
                    for x in range(j+1,len(number)):
                        if high[j]==number[x]:
                            num_idx.append(x)
                            high_num.append(high[x])
                    if number[j] in high_num:
                        if high_num.count(number[j])>=2:
                            for y in range(len(high_num)):
                                if number[j]==high_num[y]:
                                    index_count+=1
                                if index_count==high_num.count(number[j]):
                                    index=num_idx[y]
                                    break
                            number.insert(index,number.pop(j))
                            number.insert(j,number.pop(index-1))
                            flag=1
                        else:
                            index=num_idx[high_num.index(number[j])]
                            number.insert(index,number.pop(j))
                            number.insert(j,number.pop(index-1))
                            flag=1
                    else:
                        if number.count(high[j])>=2:
                            for y in range(len(number)):
                                if high[j]==number[y]:
                                    index_count+=1
                                if index_count==number.count(high[j]):
                                    number.insert(y,number.pop(j))
                                    number.insert(j,number.pop(y-1))
                                    flag=1
                                    break
                        else:
                            index=number.index(high[j])
                            number.insert(index,number.pop(j))
                            number.insert(j,number.pop(index-1))
                            flag=1
                    if flag==1:
                        flag=0
                        break
   
    answer=''.join(number)
    print(f'#{test_case}',answer)
    # ///////////////////////////////////////////////////////////////////////////////////
