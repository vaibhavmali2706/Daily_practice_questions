class Solution:
    def Sum_3(self, nums, target):
        nums.sort()
        closest_sum = float('inf')
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            k = n - 1
            while l < k:
                current_sum = nums[i] + nums[l] + nums[k]
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                if current_sum < target:
                    l += 1
                elif current_sum > target:
                    k -= 1
                
        return closest_sum
s=Solution()
print(s.Sum_3([-1,2,1,-4],1))