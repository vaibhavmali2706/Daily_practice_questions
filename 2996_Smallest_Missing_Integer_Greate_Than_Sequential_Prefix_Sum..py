nums = [4,5,6,7,8,8,9,4,3,2,7]

m_largest_prefix_sum = nums[0]
lprefix_sum = nums[0]
for i in range(1, len(nums)):
    if nums[i] == nums[i-1] + 1 or i == 0:
        lprefix_sum += nums[i]
    m_largest_prefix_sum = max(m_largest_prefix_sum, lprefix_sum)
print(m_largest_prefix_sum)
while m_largest_prefix_sum in nums:
    m_largest_prefix_sum += 1
print(m_largest_prefix_sum)


