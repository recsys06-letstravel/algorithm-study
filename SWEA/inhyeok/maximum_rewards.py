import sys

sys.stdin = open("input.txt", "r")

T = int(input())

def str_swap(s, index1, index2):
    s = list(s)
    s[index1], s[index2] = s[index2], s[index1]
    return ''.join(s)

for test_case in range(1, T + 1):
    inputs = input().strip().split(" ")
    number, chance = ''.join(inputs[0]), int(inputs[1])
    changed_list = []
    first = set()
    first.add(number)
    changed_list.append(first)
    for k in range(chance):
        changed_str_set = changed_list[k]
        test = set()
        for changed_str in changed_str_set:
            for i in range(len(number)):
                for j in range(i+1, len(number)):
                    test.add(str_swap(changed_str,i,j))
        changed_list.append(test)

    max_num = 0
    for result in changed_list[-1]:
        max_num = max(max_num, int(result))

    print(f"#{test_case}", max_num)
