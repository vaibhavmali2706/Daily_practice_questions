class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        seen=set()
        for i in arr:
            if i*2 in seen or(i%2==0 and i//2 in seen):
                return True 
            seen.add(i)
        return False
    
arr=[10,2,5,3]
print(Solution().checkIfExist(arr))

class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        flag=False
        hashmap={}
        for i in range(len(arr)):
            if arr[i]*2 in hashmap:
                flag=True
            if arr[i]%2==0 and arr[i]//2 in hashmap:
                flag=True
            hashmap[arr[i]]= True
            
        return flag
print(Solution().checkIfExist(arr))