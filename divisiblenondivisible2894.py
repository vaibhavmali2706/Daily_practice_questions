n = 5
m = 6
num1=[x for x in range(1,n+1) if x%m!=0]
num2=[y for y in range(1,n+1) if y%m==0]
print(num1)
print(num2)
print(sum(num1)-sum(num2))
