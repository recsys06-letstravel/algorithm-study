class Solution:
    def isPalindrome(self, s: str) -> bool:
        sent=''
        s=s.lower()
        if s=='':
            pass
        else:
            for a in range (len(s)):
                if (48<=ord(s[a])<=57) | (97<=ord(s[a])<=122):
                    if s[a]==' ':
                        continue
                    else:
                        sent=sent+s[a]
        if len(sent)%2==0:
            if sent[:(len(sent)//2)]==sent[(len(sent)//2):][::-1]:
                answer=True
            else:
                answer=False
        else:
            if sent[:(len(sent)//2)]==sent[((len(sent)//2)+1):][::-1]:
                answer=True
            else:
                answer=False
        return answer