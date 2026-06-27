nums=[1,7,3,6,5,6]
c=-1
for i in range (len(nums)):
    left_sum=sum(nums[:i])
    right_sum=sum(nums[i+1:])
    if left_sum==right_sum:
        c=i
        break
print(c)
print("left_sum:",left_sum)
print("right_sum:",right_sum)