candies= [2,3,5,1,3]
extraCandies = 3
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        m=max(candies)
        res=[]
        for i in candies:
            if i+extraCandies>=m:
                res.append(True)
            else:
                res.append(False)
        return res
s=Solution()
print(s.kidsWithCandies(candies, extraCandies))
        
        
        