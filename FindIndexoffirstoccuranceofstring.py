class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0,len(haystack) - len(needle) + 1):
            left_index = i
            right_index = i + len(needle) - 1;
            for j in range(left_index, right_index + 1):
                if needle[j - left_index] == haystack[j]:
                    print(needle[j - left_index],haystack[j],j,right_index);
                    if j == right_index:  
                        print(j);
                        return i
                    else:
                        continue;
                else:
                    print(j)
                    break
        return -1  