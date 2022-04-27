
k = [[1, 2, 3],
     [4, 5, 6]]
test = [[1,'B',3],
        ['B',3,'B'],
        [8, 1, 'F'],
        [7, 5, 'E']
        ]


# 시계 방향 회전
pp = [list(k[::-1]) for k in zip(*test)]
print(pp)

li = [list(k[::-1]) for k in zip(*k)]
# zip를 써서 각 인덱스의 모든 element를 한 iterator에 넣고 asterisk를 이용하여 풀어서 회전 알고리즘을 구현
# ex. k = [[1, 2, 3], [4, 5, 6]]    -> 원하는 출력 form: [[4, 1], [5, 2], [6, 3]]
# zip(*k) - 1. [1, 4]   -> k[::-1]  = [4, 1]
#           2. [2, 5]   -> k[::-1]  = [5, 2]
#           3. [3, 6]   -> k[::-1]  = [6, 3]
print(li)

# 반 시계 방향 회전
li = [list(k) for k in reversed(tuple(zip(*k)))]
# 시계 방향과 동일한 방식이지만, reversed 키워드를 사용하여 배열의 역순 탐색이 가능하게 함
# ex. k = [[1, 2, 3], [4, 5, 6]]    -> 원하는 출력 form: [[3, 6], [2, 5], [1, 4]]
# reversed(tuple(zip(*k)) - 1. [3, 6]
#                           2. [2, 5]
#                           3. [1, 4]
print(li)