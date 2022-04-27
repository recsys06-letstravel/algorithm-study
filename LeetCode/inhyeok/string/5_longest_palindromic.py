s = "babad"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left+1:right]
        answer = ""

        if len(s) < 2 or s == s[::-1]:
            return s

        for index in range(len(s)-1):
            answer = max(answer,
                         expand(index, index + 1), # 짝수
                         expand(index, index + 2), # 홀수
                         key=len
            )
        return answer

sol = Solution()
print(sol.longestPalindrome(s))