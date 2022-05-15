from collections import defaultdict
from copy import deepcopy

max_sheep = 0
def solution(info, edges):
    graph = defaultdict(list)
    for edge_from, edge_to in edges:
        graph[edge_from].append(edge_to)

    def solve(current_loc, visited, nsheep, nwolf, cango):
        global max_sheep
        if visited[current_loc]:
            return
        visited[current_loc] = True
        if info[current_loc]: # 늑대이면
            nwolf += 1
        else:
            nsheep += 1
            max_sheep = max(max_sheep, nsheep)
        if nsheep <= nwolf:
            return
        cango.extend(graph[current_loc])
        for next in cango:
            solve(next, deepcopy(visited), nsheep, nwolf, cango = [loc for loc in cango if not visited[loc] and loc != next])

    visited = [False] * len(info)
    solve(0, visited, 0, 0, [])
    return max_sheep


info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
print(solution(info, edges))