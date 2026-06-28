nums = [1,2,2,1]
k = 1
c = 0
hp = {}
for i in nums:
    a = i - k
    b = i + k

    if a in hp:
        c += hp[a]
    if b in hp:
        c += hp[b]
    hp[i] = hp.get(i,0) + 1

print(c)