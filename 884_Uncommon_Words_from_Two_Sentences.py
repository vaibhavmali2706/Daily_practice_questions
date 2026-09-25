class Solution:
    def uncommonFromSentences(self, s1: str, s2: str):
        dic={}
        for i in list(s1.split()):
            dic[i]=dic.get(i,0)+1
        for j in list(s2.split()):
            dic[j]=dic.get(j,0)+1
        return [i for i in dic if dic[i]==1]
s=Solution()
s1 = "this apple is sweet"
s2 = "this apple is sour"
print(s.uncommonFromSentences(s1,s2))