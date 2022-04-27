import sys

code = {
    "0001101": 0,
    "0011001": 1,
    "0010011": 2,
    "0111101": 3,
    "0100011": 4,
    "0110001": 5,
    "0101111": 6,
    "0111011": 7,
    "0110111": 8,
    "0001011": 9
}
sys.stdin = open("input.txt", "r")

def iscypher(s):
    return s[-1] == '1'

def verif(llist):
    if ((llist[0] + llist[2] + llist[4] + llist[6]) * 3 + llist[1] + llist[3] + llist[5] + llist[7]) % 10 == 0:
        return sum(llist)
    return 0

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    size = input().strip().split()
    n, m = int(size[0]), int(size[1])
    result = 0
    cyper_list = []
    for _ in range(n):
        test = input()
        for i in range(m-1,-1,-1):
            if cyper_list:
                break
            if test[i] == '1':
                for _ in range(8):
                    cyper_list.append(code[test[i - 6:i + 1]])
                    i = i - 7

                break
    cyper_list.reverse()
    result = verif(cyper_list)
    print(f"#{test_case}", result)

