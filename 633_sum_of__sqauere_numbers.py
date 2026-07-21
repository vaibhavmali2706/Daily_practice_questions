import math
c = 5
i=0
j=int(math.sqrt(c))
print(j)
for i in range(0, int(j)+1):
    z=i*i+j*j
    if z==c:
        print("True")
        break
    elif z>c:
        j-=1    
    elif z<c:
        i+=1

    
    

