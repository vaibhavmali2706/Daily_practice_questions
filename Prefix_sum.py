num=[1, 2, 3, 4, 5]
for i in range(1, len(num)):
    num[i]=num[i]+num[i-1]
print(num)