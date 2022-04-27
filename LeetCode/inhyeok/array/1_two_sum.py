nums = [2,7,11,15]
target = 9

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # brute_force
        def brute_force() -> list[int]:
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i,j]

        # search using "in"
        def search_in() -> list[int]:
            for i, v in enumerate(nums):
                complement = target - v
                if complement in nums[i+1:]:
                    return [i, nums[i+1:].index(complement)+i+1]

        def using_dict() -> list[int]:
            temp_dict = {}
            for i, v in enumerate(nums):
                temp_dict[v] = i

            for i, v in enumerate(nums):
                if target - v in temp_dict and i!= temp_dict[target - v]:
                    return [i, temp_dict[target - v]]

        # return brute_force() # 3736ms
        # return search_in() # 684ms
        return using_dict() # 92ms


sol = Solution()
print(sol.twoSum(nums, target))
