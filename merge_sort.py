class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
            
        def recursive_division(array):
            if len(array) <= 1:
                return array

            mid = len(array) // 2
            left_array = array[:mid]
            right_array = array[mid:]

            left_array = recursive_division(left_array)
            right_array = recursive_division(right_array)

            return merge(left_array, right_array)



        def merge(left_array,right_array):
            result=[]
            i=j=0;
            # print(left_array,right_array);
            # while(len(left_array) or len(right_array)>1):
            while(i<len(left_array) and j<len(right_array)):
                if(left_array[i]<right_array[j]):
                    result.append(left_array[i]);
                    i=i+1
                else:
                    result.append(right_array[j]);
                    j=j+1;
            result.extend(left_array[i:])
            result.extend(right_array[j:])

            return result;

        return recursive_division(nums)
