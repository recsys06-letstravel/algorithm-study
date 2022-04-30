import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# T = 10
dr = [1, 1, -1, -1, 0]  # row
dc = [1, -1, -1, 1, 0]  # col


for test_case in range(1, T + 1):
    inputs = input().strip()
    n = int(inputs)
    dessert_map = []
    for _ in range(n):
        dessert = list(map(int, input().strip().split()))
        dessert_map.append(dessert)
    result = 0
    total = []
    dessert_list = [0] * 120

    Max_count = -1
    def circuit(count: int, i: int, j: int, oi: int , oj: int, dir: int):
        global Max_count
        if dir == 4:
            return

        if i == oi and j == oj:
            if Max_count < count:
                Max_count = count
            return

        if i < 0 or j < 0 or i >= n or j >= n:
            return
        # print(i, j, len(dessert_map), len(dessert_map[0]))
        if dessert_list[dessert_map[i][j]] == 0:
            # 방향 그대로
            dessert_list[dessert_map[i][j]] = 1
            circuit(count + 1, i + dr[dir], j + dc[dir], oi, oj, dir)
            # 방향 꺽어서
            circuit(count + 1, i + dr[dir+1], j + dc[dir+1], oi, oj, dir + 1)
            dessert_list[dessert_map[i][j]] = 0
        else:
            return

    for i in range(0, n-2):
        for j in range(1, n-1):
            dessert_list[dessert_map[i][j]] = 1
            circuit(1, i+1, j+1, i, j, 0)
            dessert_list[dessert_map[i][j]] = 0

    print(f"#{test_case}", Max_count)

        # # right
        # for k in range(times+1):
        #     now_i, now_j = now_i + k, now_j + k
        #     cookie_list.append(dessert_map[now_i][now_j])
        # # bottom
        # for k in range(times+1):
        #     now_i, now_j = now_i + k, now_j - k
        #     cookie_list.append(dessert_map[now_i][now_j])
        # # left
        # for k in range(times+1):
        #     now_i, now_j = now_i - k, now_j - k
        #     cookie_list.append(dessert_map[now_i][now_j])
        # # up
        # for k in range(times+1):
        #     now_i, now_j = now_i - k, now_j + k
        #     cookie_list.append(dessert_map[now_i][now_j])
    #
    #
    # print(f"#{test_case}", result)
    # 아 잘못생각~!~!~~~~~~~~~~~~~~!!!!!!!!!!!!!!!!
    # for i in range(1, n-1):
    #     for j in range(1, n-1):
    #         alone.append([i,j])
    #         y, x = i + 1, j + 1
    #         before = [i, j]
    #         # 오른쪽 대각선
    #         while y < n - 1 and x < n - 1:
    #             more_y, more_x = y + 1, x - 1
    #             more_before = [y, x]
    #             while more_y < n - 1 and more_x > 0:
    #
    #                 more_now = more_before + [more_y, more_x]
    #                 more_before = more_now
    #                 left_big.append(more_now)
    #                 more_y, more_x = more_y + 1, more_x - 1
    #
    #             now = before + [y, x]
    #             before = now
    #             right.append(now)
    #
    #             y, x = y + 1, x + 1
    #         y, x = i + 1, j - 1
    #         before = [i, j]
    #         while y < n - 1 and x > 0:
    #             now = before + [y,x]
    #             before = now
    #             left.append(now)
    #             y, x = y + 1, x - 1

    # print(alone)
    # print(right)
    # print(left)
    # print(right_big)
    # print(left_big)
    # # 상 하 좌 우
    # def check_all(y, x):
    #     route = [dessert_map[y-1][x], dessert_map[y][x+1], dessert_map[y+1][x], dessert_map[y][x-1]]
    #     if len(set(route)) != 4:
    #         # print("same dessert_all", y, x)
    #         return []
    #     return route
    # # for right direction
    # def check_right_bottom(y, x):
    #     route = [dessert_map[y][x+1], dessert_map[y+1][x]]
    #     if len(set(route)) != 2:
    #         # print("same dessert_right")
    #         return []
    #     return route
    #
    # def check_left_bottom(y, x):
    #     route = [dessert_map[y+1][x], dessert_map[y][x-1]]
    #     if len(set(route)) != 2:
    #         # print("same dessert_left")
    #         return []
    #     return route
    #
    # for aa in alone:
    #     aa_result = check_all(aa[0], aa[1])
    #     if len(set(aa_result)) == 4:
    #         result_list.append(len(set(aa_result)))
    #         # 왼쪽 대각선
    #
    # for rr in right:
    #     rr_result = check_all(rr[0], rr[1])
    #     tmp = rr.pop(0)
    #     tmp2 = rr.pop(0)
    #     length = 0
    #     for index in range(0, len(rr), 2):
    #         rr_result += check_right_bottom(rr[index], rr[index+1])
    #         length += 1
    #
    #     if len(set(rr_result)) == 4 + 2 * length:
    #         result_list.append(len(set(rr_result)))
    #
    #
    # for ll in left:
    #     ll_result = check_all(ll[0], ll[1])
    #     tmp = ll.pop(0)
    #     tmp2 = ll.pop(0)
    #     length = 0
    #     for index in range(0, len(ll), 2):
    #         ll_result += check_left_bottom(ll[index], ll[index+1])
    #         length += 1
    #
    #     if len(set(ll_result)) == 4 + 2 * length:
    #         result_list.append(len(set(ll_result)))
    #
    # if result_list:
    #     result = max(result_list)
    # else:
    #     result = -1
    # print(f"#{test_case}", result)
