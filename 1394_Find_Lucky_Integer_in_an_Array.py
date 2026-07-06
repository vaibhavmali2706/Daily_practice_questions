arr=[2, 2, 3, 4]
hp = {}

for i in arr:
    hp[i] = hp.get(i, 0) + 1

res = -1

for key, value in hp.items():
    if key == value:
        res = max(res, key)

print(res)