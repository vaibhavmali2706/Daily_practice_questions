prices = [2,1,2,1,0,1,2]
m=0
a=0
b=1

for i in range(b,len(prices)):
    if prices[i]>prices[a]:
        cm=prices[i]-prices[a]
        m=max(m,cm)
    else:
        a=i
    
print(m)
    