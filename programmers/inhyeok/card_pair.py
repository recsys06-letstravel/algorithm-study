from itertools import permutations
from collections import defaultdict
from copy import deepcopy
import sys

max_count = 0

# def move_cost(board, start, end):
#
#
# def solve(board, position, case, y, x, cost):



# i 번째부터 거리재기

def solution(board, r, c):
    position = defaultdict(list)
    answer = float('inf')
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                position[board[i][j]].append([i,j])

    for case in permutations(position.keys(), len(position)):
        answer = min(answer, solve(deepcopy(board), case, r, c, 0))
    return answer

board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r = 1
c = 0
print(solution(board, r, c))