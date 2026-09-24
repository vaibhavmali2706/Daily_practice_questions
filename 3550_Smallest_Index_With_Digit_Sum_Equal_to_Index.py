nums=[1,10,11]
class solution:
    def findindex(self,nums):
        indexi=-1    
        
        for i,j in enumerate(nums):
            sumi=0
            while(j>0):
                a=j%10
                sumi+=a
                j=j//10
                
            if i == sumi:
                
                indexi=i
                break
        return indexi
s=solution()
print(s.findindex(nums))

