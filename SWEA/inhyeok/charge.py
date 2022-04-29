import sys
import heapq
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    inputs = input().strip().split(" ") # m 과 a 를 받고
    m, a = int(inputs[0]), int(inputs[1])
    move_a = list(map(int, input().strip().split())) # a의 이동정보
    move_b = list(map(int, input().strip().split())) # b의 이동정보
    ap_info = []
    a_sum = 0
    b_sum = 0
    result = 0

    for i in range(a):
        ap = list(map(int, input().strip().split()))
        ap_info.append(ap + [i+1])

    charge_map = [[0] * 10 for _ in range(10)]

    movement = {
        0: (0, 0),
        1: (-1, 0),
        2: (0, 1),
        3: (1, 0),
        4: (0, -1)
    }

    # 지도에 저장소 추가
    def add_charge_range(y, x, a, power, number):
        if x >= 10 or x < 0 or y >= 10 or y < 0 or a < 0:
            return
        if charge_map[y][x]:
            charge_map[y][x].add((power, number))
        else:
            charge_map[y][x] = set()
            charge_map[y][x].add((power, number))

        add_charge_range(y + 1, x, a - 1, power, number)
        add_charge_range(y - 1, x, a - 1, power, number)
        add_charge_range(y, x + 1, a - 1, power, number)
        add_charge_range(y, x - 1, a - 1, power, number)

    for ap in ap_info: # 지도에 충전소 추가
        add_charge_range(ap[1]-1, ap[0]-1, ap[2], ap[3], ap[4])

    a_y, a_x = 0, 0
    b_y, b_x = 9, 9
    for step in range(0, m+1):
        a_candidate = []
        b_candidate = []
        a_max = 0
        b_max = 0
        a_cand = ()
        b_cand = ()
        result_a_b = []
        if charge_map[a_y][a_x]: # charging
            for charge_set in charge_map[a_y][a_x]:
                a_candidate.append(charge_set)

        if charge_map[b_y][b_x]: # charging
            for charge_set in charge_map[b_y][b_x]:
                b_candidate.append(charge_set)

        # ------------------------------------------
        # 둘다 없을때
        if len(a_candidate) == 0 and len(b_candidate) == 0:
            a_max = 0

        # a 만 있을때
        elif len(a_candidate) != 0 and len(b_candidate) == 0:
            for cand in a_candidate:
                a_max = max(a_max, cand[0])
        # b 만 있을때
        elif len(a_candidate) == 0 and len(b_candidate) != 0:
            for cand in b_candidate:
                b_max = max(b_max, cand[0])
        # 둘다 있을때
        else:
            for cand_a in a_candidate:
                for cand_b in b_candidate:
                    if cand_a == cand_b:
                        result_a_b.append(cand_a[0])
                    else:
                        result_a_b.append(cand_a[0] + cand_b[0])

            a_max = max(result_a_b)
        # ------------------------------------------

        # a,b 둘다 있을때

        # if a_candidate and b_candidate: # 둘다 있을때
        #     a_b_set = set()# 중복제거
        #     for a_set in a_candidate:
        #         a_b_set.add(a_set)
        #     for b_set in b_candidate:
        #         a_b_set.add(b_set)
        #     # print(a_candidate, b_candidate)
        #     # print(a_b_set)
        #     # 같은놈이 하나밖에 없을때 반반함
        #     if len(a_b_set) == 1:
        #         for a_b in a_b_set:
        #             a_max = a_b[0] // 2
        #             b_max = a_b[0] // 2
        #     # A가 선택지가 1이라 B가 약한놈 선택해야 할때
        #     elif len(a_candidate) == 1:
        #         for temp in a_candidate:
        #             a_max = temp[0]
        #             a_cand = temp
        #
        #         a_b_set.remove(a_cand)
        #         for a_b in a_b_set:
        #             b_max = max(b_max, a_b[0])
        #
        #     # b가 1이라 A가 약한놈 선택해야 할때
        #     elif len(b_candidate) == 1:
        #         for temp in b_candidate:
        #             b_max = temp[0]
        #             b_cand = temp
        #
        #         a_b_set.remove(b_cand)
        #         for a_b in a_b_set:
        #             a_max = max(a_max, a_b[0])
        #     # 둘다 둘 이상의 BC를 가지고 있을때
        #     else:
        #         for temp in a_candidate:
        #             if a_max < temp[0]:
        #                 a_max = temp[0]
        #                 a_cand = temp
        #
        #         if a_cand in b_candidate:
        #             b_candidate.remove(a_cand)
        #         a_candidate.remove(a_cand)
        #         for temp in b_candidate + a_candidate:
        #             b_max = max(b_max, temp[0])
        #         for temp in a_candidate:
        #             b_max = max(b_max, temp[0])
        #
        # elif len(a_candidate) != 0 and len(b_candidate) == 0: # A 있으면
        #     for a_set in a_candidate:
        #         a_max = max(a_max, a_set[0])
        #
        # elif len(b_candidate) != 0 and len(a_candidate) == 0: # B 있으면
        #     for b_set in b_candidate:
        #         b_max = max(b_max, b_set[0])

        # print(a_max, b_max)
        a_sum += a_max
        b_sum += b_max
        # print(step, a_max, b_max, a_candidate, b_candidate)
        if step == m:
            continue
        a_y, a_x = a_y + movement[move_a[step]][0], a_x + movement[move_a[step]][1]
        b_y, b_x = b_y + movement[move_b[step]][0], b_x + movement[move_b[step]][1]


    # print(movement[move_a[0]][0])

    # for aaa in charge_map:
    #     print(aaa)
    # print(a_sum)
    # print(b_sum)
    result = a_sum + b_sum
    # print(a_sum + b_sum)
    # print("---------------")
    #
    print(f"#{test_case}", result)
