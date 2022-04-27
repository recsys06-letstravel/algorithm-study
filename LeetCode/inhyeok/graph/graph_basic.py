graph = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6,7],
    6: [],
    7: [3],
}


def dfs(v, discovered = []):
    discovered.append(v)
    print("visit:" , v)
    for w in graph[v]:
        if w not in discovered: # 방문하지 않았다면
            discovered = dfs(w, discovered)

    return discovered


def dfs_stack(v):
    stack = []
    stack.append(v)
    discovered = []
    while stack:
        w = stack.pop()
        if w not in discovered:
            discovered.append(w)
            for next in graph[w]:
                stack.append(next)

    return discovered


def bfs(v):
    queue = []
    queue.append(v)
    discovered = []
    while queue:
        w = queue.pop(0)
        if w not in discovered:
            discovered.append(w)
            for next in graph[w]:
                queue.append(next)
    return discovered


print(dfs(1))
print(dfs_stack(1))
print(bfs(1))

