class Solution:
    def reverseByType(self, s: str) -> str:
        i=0
        j=len(s)-1
        s=list(s)
        while i<j:
            
            if not s[i].isalpha():
                i+=1
            elif not s[j].isalpha():
                j-=1
            else:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
        i=0
        j=len(s)-1
        while i<j:
            if s[i].isalpha():
                i+=1
            elif s[j].isalpha():
                j-=1
            else:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
        return ''.join(s)
s = ")ebc#da@f("
print(Solution().reverseByType(s))