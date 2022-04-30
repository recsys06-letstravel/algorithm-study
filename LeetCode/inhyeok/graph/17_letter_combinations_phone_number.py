# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        result = []
        dict = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def dfs(index, path):
            if len(digits) == len(path):
                result.append(path)
                return

            for i in range(index, len(digits)):
                for j in dict[digits[i]]:
                    dfs(i + 1, path + j)

        if not digits:
            return []

        dfs(0, "")
        return result