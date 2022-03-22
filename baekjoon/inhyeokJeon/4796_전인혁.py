import sys

l, p, v = 1, 1, 1
count = 1
result = []
while True:
    l, p, v = map(int, sys.stdin.readline().strip().split())
    if l == 0 and p == 0 and v == 0:
        break
    full = v // p
    remainder = v % p
    if(remainder > l):
        remainder = l
    camping = full * l + remainder
    result.append("Case " +str(count) +": " + str(camping))
    count+=1

for _ in result:
    print(_)