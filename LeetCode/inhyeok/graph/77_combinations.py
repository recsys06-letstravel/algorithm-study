class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(map(list, itertools.combinations(range(1,n+1), r=k)))