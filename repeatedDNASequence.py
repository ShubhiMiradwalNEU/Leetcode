class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        set_track=set();
        for i in range(len(s)):
            left_ptr=i
            right_ptr=i+9;
            print(left_ptr,right_ptr)
            newstr = s[left_ptr:right_ptr+1]
            print(newstr)
            if newstr in s[left_ptr+1:]:
                set_track.add(newstr);
        
        return set_track
             

        