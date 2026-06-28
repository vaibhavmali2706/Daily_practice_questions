nums=[42,11,1,97]
hp = {}
c = 0
for i in nums:
    b = int(str(i)[::-1])
    value = i - b
    if value in hp:
        c += hp[value]
    hp[value] = hp.get(value, 0) + 1

print(c % (10**9 + 7))