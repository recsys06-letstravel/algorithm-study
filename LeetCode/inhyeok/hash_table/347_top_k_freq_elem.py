class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        result = []
        for num in counter.most_common(k):
            result.append(num[0])
        return result