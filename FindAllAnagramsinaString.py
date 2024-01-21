from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        arraylist=[]
        dic=dict();
        for i in p:
            if i in dic:
                dic[i]=dic[i]+1;
            else:
                dic[i]=1;
        window =dict();
        if(len(p)>len(s)):
            return [];
        for i in range(len(p)):

            if s[i] in window:
                window[s[i]]=window[s[i]]+1;
            else:
                window[s[i]]=1;
        print(dic);
        print(window);

        if window == dic:
            arraylist.append(0)

        for i in range(1, len(s) - len(p) + 1):
            left_char = s[i - 1]
            right_char = s[i + len(p) - 1]

            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]
            if(right_char) in window:
                window[right_char] += 1
            else:
                window[right_char] =1


            if window == dic:
                arraylist.append(i)

        return arraylist
