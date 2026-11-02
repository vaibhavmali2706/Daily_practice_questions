class Solution(object):
    def validPalindrome(self, s):
        i=0
        j=len(s)-1
        carry=1
        def isPalindrome(s, i, j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        while i<j:
            if s[i]!=s[j]:
                if carry==0:
                    return False
                return isPalindrome(s, i+1, j) or isPalindrome(s, i, j-1)
            i+=1
            j-=1
        return True
s=Solution()
print(s.validPalindrome("abca"))