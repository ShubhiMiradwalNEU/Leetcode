class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string=s.split(" ");
        a=len(string)

        for i in range(a-1,-1,-1):
            if string[i].isalpha():
                return len(string[i])
        
        return 0
        