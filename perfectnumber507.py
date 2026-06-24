num=28
sum=0

    

    
for i in range(1,int(num**0.5)+1):
    if num%i==0:
        sum=sum+i 
print(sum*2)