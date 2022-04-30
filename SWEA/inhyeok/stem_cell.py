import sys
import heapq
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    inputs = input().strip().split(" ")
    n, m, k = int(inputs[0]), int(inputs[1]), int(inputs[2])


    cell_list = [[0] * 650 for _ in range(650)]
    will_be = [] # live, y, x, times
    hq = [] # live, y, x
    for i in range(n):
        states = list(map(int, input().strip().split()))
        for j in range(m):
            if states[j]:
                will_be.append([states[j], 300+i, 300+j, states[j]])
                cell_list[300+i][300+j] = states[j]

    def spread(live, i, j):
        if cell_list[i+1][j] == 0:
            cell_list[i+1][j] = live
            will_be.append([live, i+1, j, live+1])

        if cell_list[i-1][j] == 0:
            cell_list[i-1][j] = live
            will_be.append([live, i-1, j, live+1])

        if cell_list[i][j+1] == 0:
            cell_list[i][j+1] = live
            will_be.append([live, i, j+1, live+1])

        if cell_list[i][j-1] == 0:
            cell_list[i][j-1] = live
            will_be.append([live, i, j-1, live+1])

    for times in range(1, k+1):
        while hq: # 활성화 된 것들을 뿌려준다.
            activated = heapq.heappop(hq)
            live, i, j = activated
            spread(-live, i, j)
            if times - live <= k+1:
                cell_list[i][j] = -1

        deleted = []
        for i, item in enumerate(will_be):
            item[3] -= 1
            if item[3] == 0: # 활성화 된것들은 리스트에서 빼고 queue에 넣어준다.
                heapq.heappush(hq, (-item[0], item[1], item[2]))
                deleted.append(i)

        deleted.sort(reverse=True)
        for qq in deleted:
            will_be.pop(qq)

    result = 0
    for cells in cell_list:
        # print(cells[250:350])
        result += cells.count(0)
        result += cells.count(-1)

    result = 650 * 650 - result

    print(f"#{test_case}", result)