class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_counter = collections.Counter(stones)
        result = 0
        for j in jewels:
            result += stone_counter[j]
        return result