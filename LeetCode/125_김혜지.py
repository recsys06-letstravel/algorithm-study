# 125
# https://leetcode.com/problems/valid-palindrome/submissions/

class Solution(object):
    def isPalindrome(self, s):
        s = s.lower() # 모든 글자를 소문자로
        # 모든 공백과 특수문자를 제거하여 문자열을 만듦
        s = [s_w for s_w in s if s_w.isdigit() or s_w.isalpha()]       
        s = "".join(s)

        if s == s[::-1] : return True
        else : return False

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))

# Runtime: 45 ms, faster than 73.01% of Python online submissions for Valid Palindrome.
# Memory Usage: 14.7 MB, less than 53.75% of Python online submissions for Valid Palindrome.