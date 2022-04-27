class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        answer=[]
        for x in range(len(s)-1):
            s.insert(-x-1,s.pop(0))
        s.insert(0,s.pop(-1))