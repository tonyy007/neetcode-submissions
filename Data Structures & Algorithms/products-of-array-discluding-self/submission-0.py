class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_zeros = 0
        index = 0
        total = 1
        for i,num in enumerate(nums):
            if num == 0:
                count_zeros += 1
                index = i
                if count_zeros == 2:
                    return [0] * len(nums)
            else:
                total *= num
            
        to_list = []
        
        if count_zeros == 1:
            to_list = [0] * len(nums)
            to_list[index] = total
            return to_list
        else:
            to_list = nums
            for i, num in enumerate(to_list):
                to_list[i] = int(total / to_list[i])
            
            return to_list