import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
man_hole = {
    0: [],
    1: [[-1, 0], [1, 0], [0, -1], [0, 1]], # 모두
    2: [[-1, 0], [1, 0]], # 상 하
    3: [[0, -1], [0, 1]], # 좌 우
    4: [[-1, 0], [0, 1]], # 상 우
    5: [[1, 0], [0, 1]], # 하, 우
    6: [[0, -1], [1, 0]], # 하, 좌
    7: [[-1, 0], [0, -1]] # 상, 좌
}

for test_case in range(1, T + 1):
    inputs = list(map(int, input().strip().split()))
    N, M, R, C, L = int(inputs[0]), int(inputs[1]), \
                    int(inputs[2]), int(inputs[3]), \
                    int(inputs[4])
    is_man_hole = [[0] * (M+1) for _ in range(N+1)]
    man_hole_map = []
    q = []
    for _ in range(N):
        man_hole_map.append(list(map(int, input().strip().split())) + [0])
    man_hole_map.append([0] * (M+1))

    # def visit(i, j, bi, bj, time):
    #     # 벗어나면
    #     if i < 0 or i >= N or j < 0 or j >= M:
    #         # print("out of range")
    #         return
    #     # 시간이 다 지났으면
    #
    #     if time <= 1:
    #         # print("time over")
    #         return
    #     # 터널이 없으면
    #     # print(man_hole_map[i][j])
    #
    #     if man_hole_map[i][j] == 0:
    #         # print("no tunnel", i, j)
    #         return
    #     # 터널이 연결되지 않았다면
    #     check = False
    #     for before in man_hole[man_hole_map[i][j]]:
    #         if bi == i + before[0] and bj == j + before[1]:
    #             # print("connected")
    #             check = True
    #             break
    #     if check is False:
    #         # print("터널연결안됨")
    #         return
    #     # print("moving:", i, j, time)
    #     is_man_hole[i][j] = 1
    #     for next in man_hole[man_hole_map[i][j]]:
    #         # print("before:", i, j, "next:" , next)
    #         # print("manhole:" , is_man_hole[i + next[0]][j + next[1]], man_hole_map[i + next[0]][j + next[1]])
    #         if is_man_hole[i + next[0]][j + next[1]] == 0 and man_hole_map[i + next[0]][j + next[1]] != 0:
    #             visit(i + next[0], j + next[1], i, j, time-1)

    def bfs():
        is_man_hole[R][C] = 1
        q.append((R, C))
        while q:
            y, x = q.pop(0)
            direction = man_hole[man_hole_map[y][x]]
            if direction == []:
                continue
            for i in direction:
                dy, dx = y + i[0], x + i[1]
                if 0 <= dy < N and 0 <= dx < M and is_man_hole[dy][dx] == 0 and man_hole_map[dy][dx] != 0:
                    next = man_hole[man_hole_map[dy][dx]]
                    for k in next:
                        my, mx = dy + k[0], dx + k[1]
                        if my == y and mx == x:
                            q.append((dy, dx))
                            is_man_hole[dy][dx] = is_man_hole[y][x] + 1

    bfs()
    # for next in man_hole[man_hole_map[R][C]]:
    #     visit(R + next[0], C + next[1], R, C, L)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if 0 < is_man_hole[i][j] <= L:
                cnt += 1

    # for x in man_hole_map:
    #     print(x)

    print(f"#{test_case}", cnt)
