nums = [4,5,0,-2,-3,1]
k = 5
hp = [0] * k
hp[0]=1

c = 0
p = 0
for i in nums:
    p = (p + i) % k

            
    c += hp[p]

    hp[p]+=1
print(c)