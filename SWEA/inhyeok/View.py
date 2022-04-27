import sys
sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    aparts = int(input())
    floor = input().strip()
    apart_list = floor.split(' ')
    apart_list = list(map(int, apart_list))
    result = 0
    for i in range(2,len(apart_list)-2):
        total_max = max(apart_list[i+2], apart_list[i+1], apart_list[i-2], apart_list[i-1])
        if apart_list[i] <= total_max:
            continue
        else:
            result += apart_list[i] - total_max

    print(f'#{test_case}', result)