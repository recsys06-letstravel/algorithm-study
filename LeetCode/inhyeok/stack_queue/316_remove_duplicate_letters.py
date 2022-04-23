# 중복된 알파벳 제거
# 순서는 바꾸지않고
# 사전순으로
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 중복 되는게 있으면 넣고
        # for char in sorted(set(s)):
        #     suffix = s[s.index(char):]
        #     if set(suffix) == set(s):
        #         return char + self.removeDuplicateLetters(suffix.replace(char,''))
        # return ''

        # stack
        counter, seen, stack = collections.Counter(s), set(), []
        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)