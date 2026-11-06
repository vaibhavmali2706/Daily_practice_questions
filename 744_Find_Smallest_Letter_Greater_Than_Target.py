class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        r=ord(target)
        res=122
        if ord(letters[-1])<=r:
            return letters[0]
        for i in letters:
            if ord(i)>r:
                res=min(res,ord(i))
        return chr(res)
        
letters = ["c","f","j"]
target = "c"
s=Solution()
print(s.nextGreatestLetter(letters, target))

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        for i in letters:
            if i>target:
                return i
        else:
            return letters[0]
letters = ["c","f","j"]
target = "c"
s=Solution()
print(s.nextGreatestLetter(letters, target))

