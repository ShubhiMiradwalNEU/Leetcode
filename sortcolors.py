class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count=[0,0,0]
        for i in range(0, len(nums)):
            if(nums[i]==0):
                count[0]=count[0]+1;
            if(nums[i]==1):
                count[1]=count[1]+1;
            if(nums[i]==2):
                count[2]=count[2]+1;
        
        for i in range(0, len(nums)):
            if(i<count[0]):
                nums[i]=0
            elif(i<count[0]+count[1]):      
                nums[i]=1
            else:
                nums[i]=2

        return nums[i]

        