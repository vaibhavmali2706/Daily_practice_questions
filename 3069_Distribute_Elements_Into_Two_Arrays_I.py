class Solution:
    def resultArray(self, nums):
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        for i in range(2,len(nums)):
            if arr1[-1]>arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        return arr1+arr2
nums = [1, 2, 3, 4, 5]
s= Solution()
print(s.resultArray(nums))  # Output: [1, 3, 5, 2, 4]