class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return_list = [0] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            return_list[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):

            return_list[i] *= postfix
            postfix *= nums[i]
        return return_list
