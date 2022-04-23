# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV139KOaABgCFAYh&categoryId=AV139KOaABgCFAYh&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1&&&&&&&&&&
# Flatten

for test_case in range(1, 11):
    dump_count, yellow_boxes = int(input()), list(map(int, input().strip().split()))
    for _ in range(dump_count):
        yellow_boxes[yellow_boxes.index(max(yellow_boxes))] -= 1
        yellow_boxes[yellow_boxes.index(min(yellow_boxes))] += 1
    print(f"#{test_case} {max(yellow_boxes)-min(yellow_boxes)}")
