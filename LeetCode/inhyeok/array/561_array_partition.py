class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        result = 0
        for i in range(0, len(nums), 2):
            result += min(nums[i], nums[i + 1])

        return sum(sorted(nums)[::2])
        # return result


nums = [6,2,6,5,1,2]
nums.sort()
sol = Solution()
# print(nums)
print(sol.arrayPairSum(nums))
