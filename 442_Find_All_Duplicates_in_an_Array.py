nums = [4,3,2,7,8,2,3,1]
hashmap = {}
result = []

for num in nums:
    hashmap[num] = hashmap.get(num, 0) + 1
for num, freq in hashmap.items():
    if freq > 1:
        result.append(num)
print(result)
    