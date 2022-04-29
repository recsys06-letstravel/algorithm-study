import sys
import heapq
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    inputs = input().strip().split(" ") # m 과 a 를 받고
    n, x = int(inputs[0]), int(inputs[1])
    run_way1 = []
    for _ in range(n):
        tmp = list(map(int, input().strip().split()))
        run_way1.append(tmp)

    run_way_clock_wise = [list(k) for k in reversed(tuple(zip(*run_way1)))]


    # if test_case != 3:
    #     continue
    # for way in run_way1:
    #     print(way)
    result = 0
    # 가로일 떄 좌우
    def check_possible(i,j, run_way, check): #  불가능 -1 가능하면 포지션
        k = 0

        next_list = []
        while j + k < n and k <= x:
            next_list.append(run_way[i][j + k])
            k += 1
        set_list = list(set(next_list))
        tmp = next_list[0]
        count = 0
        if check == 1:
            if run_way[i][j-1] != next_list[0] and len(next_list) < x:
                return -1, 0
        # 다 같을 때
        if len(set_list) == 1:
            return j+1, 0
        # 점프하고 난 후 에러
        if len(next_list) < x + 1 and next_list[0] != next_list[-1]:
            # print(" 점프에러 ")
            return -1, 0

        # 두 종류 초과 있을때 false
        elif len(set_list) > 2:
            # print(i, "2 종류 초과")
            return -1, 0
        # 중간에 있을 때

        # 2개 이상 차이날 때
        elif abs(set_list[0] - set_list[1]) > 1:
            return -1 , 0
        # 왼쪽 것들이 같고 오른쪽 하나만 다를 때
        elif len(set(next_list[:x])) == 1:
            if next_list[-1] - next_list[0] == 1:
                # print("jump up")
                return j + x, 1

            else:
                # print("jump error")
                return j + 1, 0

        # 오른쪽 것들이 같고 왼쪽 하나만 다를 때
        elif len(set(next_list[1:])) == 1:
            if next_list[-1] - next_list[0] == -1:
                # print("jump down")
                return j + x + 1, 1

            elif next_list[-1] - next_list[0] == 1:
                # print("error")
                return -1, 0

            else:
                # print("jump error")
                return j + 1, 0
        # elif len(set(next_list[:x])) >= 2 and len(set(next_list[1:])) >= 2:
        #     print(i,j, "2 중간 eerror")
        #     return -1, 0

        for temp in next_list[1:]:
            if tmp != temp:
                tmp = temp
                count += 1

        if count >= 2:
            return -1, 0

        return j + 1, 0
            # 오른쪽 것들이 같고 왼쪽 하나만 다를 때

    for i in range(n):
        possible = True
        now_position = 0
        j = 0
        check = 0
        while j < n:
            # print(i, j)
            j, check = check_possible(i, j,run_way1, check)
            if j == -1:
                possible = False
                break
            # if tmp == -1:
            #     possible = False
            #     break
            # else:
            #     j = tmp
            #
            # j += 1
        # for j in range(n):
        #     next_info = []
        #     for k in range(j, n):
        #         if k - j > x:
        #             break
        #         if k - j == x:
        #             if abs(run_way[i][j] - run_way[i][j]) > 1:
        #                 break
        #             next_info.append(run_way[i][k])
        #
        #         if run_way[i][j] == run_way[i][j]:
        #             next_info.append(run_way[i][k])
        #
        #
        #     for info in next_info:
        #
        #     k = 1
        #     while j + k < n:
        #     now_height = run_way[i][j]
        #     next_x_height = []
        #     if j + 1 < n:
        #         # 높이가 같을때
        #         if possible is False:
        #             break
        #         if run_way[i][j] == run_way[i][j+1]:
        #             continue
        #         elif abs(run_way[i][j] - run_way[i][j+1]) > 1:
        #             possible = False
        #             break
        #         else: # 다리를 놓을 수 있을 때
        #             tmp = 1
        #             depth = 0
        #             if tmp + j < n:
        #                 depth = run_way[i][j] - run_way[i][j + tmp]
        #                 tmp += 1
        #             while tmp <= x and tmp + j < n:
        #                 if depth == run_way[i][j] - run_way[i][j + tmp]:
        #                     tmp += 1
        #                 else:
        #                     possible = False
        #                     break
        # 왼쪽 부터
        if possible:
            result += 1

    print("-" * 30)
    for i in range(n):
        possible = True
        now_position = 0
        j = 0
        while j < n:
            # print(i, j)
            j, check = check_possible(i,j,run_way_clock_wise, check)
            if j == -1:
                possible = False
                break

        if possible:
            result += 1
    # 상하일 때 위 아래
    # for way in run_way_clock_wise:
    #     print(way)
    print(f"#{test_case}", result)
    # print("-" * 30)

