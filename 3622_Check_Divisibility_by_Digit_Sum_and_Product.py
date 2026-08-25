n = 10

class Solution:
    def check(self, n: int) -> bool:
        s=0
        p=1
        ab=n
        while ab>0:
            d=ab%10
            s+=d
            p*=d
            ab//=10
        print(s+p)
        return n%(s+p)==0
s=Solution()

print(s.check(n))
