
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        def dfs(csum, index, path):
            if csum < 0:
                return

            elif csum == 0:
                result.append(path)
                return

            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])

        print(result)

candidates = [2,3,5]
temp = Solution()
temp.combinationSum(candidates, 8)