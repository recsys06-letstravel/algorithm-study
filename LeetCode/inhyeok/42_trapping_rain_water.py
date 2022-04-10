height = [0,1,0,2,1,0,1,3,2,1,2,1]
class Solution:
    def trap(self, height: list[int]) -> int:
        # two pointer # 123ms
        # left = 0
        # right = len(height)-1
        # volume = 0
        # left_max, right_max = height[left], height[right]
        # while left < right:
        #     left_max = max(left_max, height[left])
        #     right_max = max(right_max, height[right])
        #     if left_max <= right_max:
        #         volume += left_max - height[left]
        #         left += 1
        #     else:
        #         volume += right_max - height[right]
        #         right -=1

        # with stack  어렵다. # 100ms
        stack = []
        volume = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]: # 더 큰것이 나타나면
                top = stack.pop()
                if not len(stack):
                    break
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
                volume += distance * waters


            stack.append(i)


        return volume


sol = Solution()
print(sol.trap(height))