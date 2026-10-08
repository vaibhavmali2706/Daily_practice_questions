class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        d=0
        sq=[]
        for i in s:
            if i == '(':
                if d>0:
                    sq.append(i)
                d+=1
            else:
                d-=1
                if d>0:
                    sq.append(i)
        return ''.join(sq)
    def removeOuterParentheses(self, s: str) -> str:
            d=0
            sq=''
            for i in s:
                if i == '(':
                    if d>0:
                        sq += i
                    d+=1
                else:
                    d-=1
                    if d>0:
                        sq += i
            return sq
s = "(()())(())"
solution = Solution()
print(solution.removeOuterParentheses(s))