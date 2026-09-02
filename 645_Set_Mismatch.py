class Solution:
    def findErrorNums(self, nums):
        hashmap={}
        dupl=-1
        missing=-1
        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
            if hashmap[i]==2:
                dupl=i
        for i in range(1, len(nums) + 1):
            if i not in hashmap:
                missing=i
                break
        return [dupl, missing]

nums=[1,1,2,4]
sol=Solution()
print(sol.findErrorNums(nums))