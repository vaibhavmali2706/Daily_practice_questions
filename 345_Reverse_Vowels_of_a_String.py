class solition:
    def checkstring(self,s):
        
        vowels="aeiouAEIOU"
        i=0
        s=list(s)
        j=len(s)-1
        while i<j:
            if s[i] not in vowels:
                i+=1
            if s[j] not in vowels:
                j=j-1
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        return(''.join(s))


se = "leetcode"

sol=solition()
print(sol.checkstring(se))

