class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        abc=len(nums);
        if not any(map(bool, nums)):
            return '0'

        for i in range(len(nums)):
            nums[i]=str(nums[i]);


        def compare(x, y):
            return int(nums[x] + nums[y]) > int(nums[y] + nums[x])

        for x in range(len(nums)):
            y=x+1
            while y<abc:
                if not compare(x,y):
                    nums[x], nums[y]=nums[y], nums[x];
                    # print(nums);
                y=y+1;

        return "".join(nums)        
        