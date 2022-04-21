# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1

import sys

T = 10

for test_case in range(1, T + 1):   
    length = int(input())
    building_height = list(map(int, sys.stdin.readline().strip().split(" ")))
    result = 0
    for i in range(length):
        if i not in [0, 1, length-1, length-2]:
            if building_height[i] > building_height[i-1] and building_height[i] > building_height[i-2] and \
                building_height[i] > building_height[i+1] and building_height[i] > building_height[i+2]:
                
                max_height_building = max([building_height[i-1], building_height[i-2], building_height[i+1], building_height[i+2]])
                result += (building_height[i]-max_height_building)


    print(f"#{test_case} {result}")




