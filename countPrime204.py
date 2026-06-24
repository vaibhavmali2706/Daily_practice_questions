num=1
count=0
i=2

while(i<num):
    j=2
    while(j<i):
        if i%j==0:
            break
        j+=1
    else:
        count+=1
    i+=1
print(count)
        
    