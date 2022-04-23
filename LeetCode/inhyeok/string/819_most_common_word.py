class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        text_list = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

        counts = collections.Counter(text_list)
        return counts.most_common(1)[0][0]