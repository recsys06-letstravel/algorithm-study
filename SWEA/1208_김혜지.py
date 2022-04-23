# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV139KOaABgCFAYh&categoryId=AV139KOaABgCFAYh&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1&&&&&&&&&&
# Flatten

T = 10

for test_case in range(1, T + 1):
    dump_count = int(input())
    yellow_boxes = list(map(int, input().strip().split()))

    for _ in range(dump_count):
        max_height = max(yellow_boxes)
        max_idx = yellow_boxes.index(max_height)

        min_height = min(yellow_boxes)
        min_idx = yellow_boxes.index(min_height)

        yellow_boxes[max_idx] -= 1
        yellow_boxes[min_idx] += 1

    print(f"#{test_case} {max(yellow_boxes)-min(yellow_boxes)}")
