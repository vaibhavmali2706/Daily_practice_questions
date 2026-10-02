s = "aabc"
x = "a"
y = "c"
class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        if ord(x) > ord(y):
            return ''.join(sorted(s))
        else:
            return ''.join(sorted(s, reverse=True))
print(Solution().rearrangeString(s, x, y))