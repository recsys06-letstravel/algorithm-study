import sys

sys.stdin = open("sample_input.txt", "r")

def clock_wise(str):
    treasure = str.replace('', ' ').split()
    treasure.insert(0, treasure.pop())
    return ''.join(treasure)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    size = input().strip().split()
    n, m = int(size[0]), int(size[1])
    treasure = input().strip()
    magic_num = n // 4
    result = ""
    treasure_set = set()
    for _ in range(magic_num):
        treasure_set.add(treasure[0:magic_num])
        treasure_set.add(treasure[magic_num:magic_num*2])
        treasure_set.add(treasure[magic_num*2:magic_num*3])
        treasure_set.add(treasure[magic_num*3:magic_num*4])
        treasure = clock_wise(treasure)

    treasure_list = []
    for tt in treasure_set:
        treasure_list.append(tt)
    treasure_list.sort(reverse=True)
    print(f"#{test_case}", int(treasure_list[m-1], 16))

