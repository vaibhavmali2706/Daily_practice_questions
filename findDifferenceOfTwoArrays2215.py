nums1 = [1,2,3]
nums2 = [2,4,6]
nums11=list(set(i for i in nums1 if i not in nums2))
nums22=list(set(i for i in nums2 if i not in nums1))
print([nums11,nums22])