# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Time Over

        # result = []
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         else:
        #             if nums[j] == 1:
        #                 continue
        #             product = product * nums[j]
        #
        #     result.append(product)
        p = 1
        out = []
        for i in range(len(nums)):
            out.append(p)
            p = p * nums[i]
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] = (p * out[i])
            p = p * nums[i]

        # result.reverse()
        return out

nums = [1,2,3,4]
nums.sort()
sol = Solution()
# print(nums)
print(sol.productExceptSelf(nums))
