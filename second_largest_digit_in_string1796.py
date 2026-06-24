s ="sjhtz8344"
nums=[int(ch) for ch in s if ch.isdigit()]
to=-1
so=-1
for i in nums:
    if i>to:
        so=to
        to=i
    elif to>i>so:
        so=i
print(nums)
print(so)