class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_len = start = 0
        for i, char in enumerate(s):
            # 이미 나왔던 알파벳이라면
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:  # 아니면
                max_len = max(max_len, i - start + 1)

            used[char] = i
        return max_len

