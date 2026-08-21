class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        hashmap = {}
        while(n>0):
            num=n%10
            hashmap[num]=hashmap.get(num,0)+1
            n=n//10
        res=0
        for k,v in hashmap.items():
            r=k*v
            res+=r
        return res
        
s= Solution()
print(s.digitFrequencyScore(121))  # Output: 4