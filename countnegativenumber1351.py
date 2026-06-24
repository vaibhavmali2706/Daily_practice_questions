matrix=[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
count=0
for row in matrix:
    for val in row:
        if val < 0:
            count=count+1
print(count)