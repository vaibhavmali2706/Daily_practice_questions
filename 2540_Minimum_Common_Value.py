class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        nums1.sort()
        nums2.sort()
        i=0
        j=0
        if nums1[0]>nums2[-1] or nums2[0]>nums1[-1]:
            return -1
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                return nums1[i]
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        return -1
print(Solution().getCommon([1,2,3],[2,4]))
class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        s=set(nums1)
        for i in nums2:
            if i in s:
                return i
        return -1
print(Solution().getCommon([1,2,3],[2,4]))