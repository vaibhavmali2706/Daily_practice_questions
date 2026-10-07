n = [1,1,1,2,2,3]
k = 2
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        l=[]
        for i in nums:
            
            if nums.count(i)>=k and i not in l:
                l.append(i)
        return l
print(Solution().topKFrequent(n,k))