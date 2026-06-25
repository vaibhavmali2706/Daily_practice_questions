nums = [2, 7, 11, 15]
target = 13
hp = {}

for i in range(len(nums)):
    diff = target - nums[i]

    if diff in hp:
        print([hp[diff], i])

    hp[nums[i]] = i