class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                last = stack.pop()
                ans[last] = i - last
            stack.append(i)

        return ans