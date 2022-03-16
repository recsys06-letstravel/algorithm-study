# https://www.acmicpc.net/problem/4796
# 캠핑

import sys
camping_warning = list()
while True:
    l, p, v = list(map(int, sys.stdin.readline().strip().split()))
    camping_warning.append([l, p, v])
    if [l, p, v] == [0, 0, 0] : break


for idx, [l, p, v] in enumerate(camping_warning):
    if [l, p, v] == [0, 0, 0] : break
    if v%p <= l : result = v//p*l + v%p
    else : result = v//p*l + l
    print(f"Case {idx+1}: {result}")
