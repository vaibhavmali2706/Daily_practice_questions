nums=[1,2,1,4]
"""if nums==sorted(nums) or nums==sorted(nums,reverse=True):
    print(True)"""
def inc(nums):
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            return False
    return True

def dec(nums):
    for i in range(len(nums)-1):
        if nums[i]<nums[i+1]:
            return False
    return True

if inc(nums) or dec(nums):
    print(True)