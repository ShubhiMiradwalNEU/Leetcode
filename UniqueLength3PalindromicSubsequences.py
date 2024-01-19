class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        maxcount=0
        h=set()
        for i in range(0,26):
            aef = chr(i + ord('a'))
            if aef in s:
                first_index=s.index(aef);
                last_index=s.rindex(aef);
                for j in range(first_index+1, last_index):
                    h.add(aef + s[j]);
                print(h)
        return len(h)
