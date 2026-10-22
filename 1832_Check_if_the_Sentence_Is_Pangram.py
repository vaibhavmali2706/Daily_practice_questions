class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
s=Solution().checkIfPangram("thequickbrownfoxjumpsoverthelazydog")
print(s)
