import collections
import heapq
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))
        hq = [(0, k)]
        dist = collections.defaultdict(int)
        while hq:
            weight, node = heapq.heappop(hq)
            if node not in dist:
                dist[node] = weight
                for next_weight, next in graph[node]:
                    total_weight = next_weight + weight
                    heapq.heappush(hq, (total_weight, next))

        if len(dist) == n:
            return max(dist.values())
        return -1
temp = Solution()
print(temp.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
