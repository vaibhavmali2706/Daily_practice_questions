class solution:
    def reverseDegree(self, s: str):
        tar=0
        for i in range(len(s)):
            tar+=(ord('z')-ord(s[i])+1)*(i+1)
        return tar
s = "zaza"
sol=solution()
print(sol.reverseDegree(s))
    