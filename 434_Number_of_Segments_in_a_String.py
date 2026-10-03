st = "Hello, my name is John"
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())   
s = Solution()
print(s.countSegments(st))

class Solution1:
    def countSegments(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            if s[i] != ' ' and (i == 0 or s[i-1] == ' '):
                count += 1
        return count

s1 = Solution1()
print(s1.countSegments(st))