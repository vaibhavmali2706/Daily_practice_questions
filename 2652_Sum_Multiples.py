n = 9
class solution:
    def sumofmultiples(self,n):
        sumi=0
        for i in range(n+1):
            if i%3==0 or i%5==0 or i%7==0:
                sumi+=i
        return sumi
s=solution()
print(s.sumofmultiples(n))