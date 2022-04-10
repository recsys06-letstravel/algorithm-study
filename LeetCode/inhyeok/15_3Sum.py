# 세수의 합 = 0


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # brute force # Time Limit Exceeded
        # nums.sort()
        # result = []
        # for i in range(len(nums)):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     for j in range(i+1, len(nums)):
        #         if j > i+1 and nums[j] == nums[j-1]:
        #             continue
        #         for k in range(j+1, len(nums)):
        #             if k > j + 1 and nums[k] == nums[k - 1]:
        #                 continue
        #
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 result.append([nums[i], nums[j], nums[k]])
        #                 break

        # two point 1088ms
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                sums = nums[left] + nums[right] + nums[i]
                if sums > 0:
                    right -= 1
                elif sums < 0:
                    left += 1
                else:  # sum = 0
                    result.append([nums[i], nums[left], nums[right]])
                    # 모두 0 일떄 생각해서 없애주자
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -=1

                    left += 1
                    right -= 1

        return result


nums = [-1, 0, 1, 2, -1, -4]
sol = Solution()
print(sol.threeSum(nums))