nums=[3,0,1,3]
seen = set()

for x in nums:
    if x in seen:
        print(x)
    seen.add(x)