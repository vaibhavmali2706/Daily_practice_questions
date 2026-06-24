costs =[10,6,8,7,7,8]
coins = 5
r=costs.sort()
count=0
for i in costs:
    if coins>i:
        count+=1
        coins-=i
        print(coins)
print(count)
    