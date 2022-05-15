import collections
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        visited = collections.defaultdict(int)
        K = 0
        hq = [(0, src, 0)]
        while hq:
            price, city, K = heapq.heappop(hq)
            if city == dst:
                return price

            if city not in visited or visited[city] > K:
                visited[city] = K
                for next_city, next_price in graph[city]:
                    if K <= k:
                        total_price = price + next_price
                        heapq.heappush(hq, (total_price, next_city, K + 1))

        return -1

temp = Solution()
print(temp.findCheapestPrice(13, [[11,12,74],[1,8,91],[4,6,13],[7,6,39],[5,12,8],[0,12,54],[8,4,32],[0,11,4],[4,0,91],[11,7,64],[6,3,88],[8,5,80],[11,10,91],[10,0,60],[8,7,92],[12,6,78],[6,2,8],[4,3,54],[3,11,76],[3,12,23],[11,6,79],[6,12,36],[2,11,100],[2,5,49],[7,0,17],[5,8,95],[3,9,98],[8,10,61],[2,12,38],[5,7,58],[9,4,37],[8,6,79],[9,0,1],[2,3,12],[7,10,7],[12,10,52],[7,2,68],[12,2,100],[6,9,53],[7,4,90],[0,5,43],[11,2,52],[11,8,50],[12,4,38],[7,9,94],[2,7,38],[3,7,88],[9,12,20],[12,0,26],[10,5,38],[12,8,50],[0,2,77],[11,0,13],[9,10,76],[2,6,67],[5,6,34],[9,7,62],[5,3,67]], 10, 1, 10))