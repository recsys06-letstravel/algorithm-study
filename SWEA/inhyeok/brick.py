import sys
import copy
sys.stdin = open("sample_input.txt", "r")


def after_break(bricks: list) -> list:
    result = [[0] * len(bricks[0]) for _ in range(len(bricks))]
    temp2 = []
    for j in range(len(bricks[0])):
        temp = []
        for i in range(len(bricks) - 1, -1, -1):
            if bricks[i][j]:
                temp.append(bricks[i][j])
        temp2.append(temp)

    for i in range(len(temp2)):
        for j, val2 in enumerate(temp2[i]):
            result[len(bricks) - 1 - j][i] = val2

    return result


# 한번 떨어뜨렸을때 남는 리스트
def brick_break(brick: list, index: int) -> list:
    stack = []
    result = copy.deepcopy(brick)
    check = 0
    for y in range(len(brick)):
        if brick[y][index] == 1:
            result[y][index] = 0
            return result
        elif brick[y][index] > 1:
            check = 1
            stack.append([y, index, brick[y][index]])
            result[y][index] = 0
            break
    while stack:
        y, x, power = stack.pop()
        for length in range(1, power):
            left = x - length
            right = x + length
            bottom = y + length
            up = y - length
            # go left
            if left >= 0:
                if result[y][left] == 1:
                    result[y][left] = 0
                elif result[y][left] > 1:
                    stack.append([y, left, brick[y][left]])
                    result[y][left] = 0
            # right
            if right < len(result[0]):
                if result[y][right] == 1:
                    result[y][right] = 0
                elif result[y][right] > 1:
                    stack.append([y, right, brick[y][right]])
                    result[y][right] = 0
            # bottom
            if bottom < len(result):
                if result[bottom][x] == 1:
                    result[bottom][x] = 0
                elif result[bottom][x] > 1:
                    stack.append([bottom, x, brick[bottom][x]])
                    result[bottom][x] = 0

            if up >= 0:
                if result[up][x] == 1:
                    result[up][x] = 0
                elif result[up][x] > 1:
                    stack.append([up, x, brick[up][x]])
                    result[up][x] = 0
    if check:
        result = after_break(result)
    return result


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    size = input().strip().split()
    # 구슬의 수, w x h 배열
    n, w, h = int(size[0]), int(size[1]), int(size[2])
    original = []
    for i in range(h):
        temp = list(map(int, input().strip().split()))
        original.append(temp)
    min_nonzero = 225  # 임의 15 x 15
    for i in range(w):
        first_list = brick_break(original, i)
        min_nonzero = min(min_nonzero,
                          w * h - sum(first_list[t].count(0) for t in range(h)))
        for j in range(w):
            if n == 1:
                break
            second_list = brick_break(first_list, j)
            min_nonzero = min(min_nonzero,
                              w * h - sum(second_list[t].count(0) for t in range(h)))
            for k in range(w):
                if n == 2:
                    break
                third_list = brick_break(second_list, k)
                min_nonzero = min(min_nonzero,
                                  w * h - sum(third_list[t].count(0) for t in range(h)))
                for q in range(w):
                    if n == 3:
                        break
                    forth_list = brick_break(third_list, q)
                    min_nonzero = min(min_nonzero,
                                      w * h - sum(forth_list[t].count(0) for t in range(h)))

    print(f"#{test_case}", min_nonzero)
