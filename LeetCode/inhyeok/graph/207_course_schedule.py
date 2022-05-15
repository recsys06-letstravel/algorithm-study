import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()
        visited = set()
        def dfs(i):
            if i in traced:
                return False

            if i in visited:
                return True
            traced.add(i)
            visited.add(i)
            for next in graph[i]:
                if not dfs(next):
                    return False
            traced.remove(i)

            return True

        for i in list(graph):
            if not dfs(i):
                return False
        return True

temp = Solution()
print(temp.canFinish(2, [[1,0]]))