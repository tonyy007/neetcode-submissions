class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return_list = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1

            right = len(nums) - 1
            number = nums[i]
            while left < right:

                if nums[left] + number + nums[right] == 0:
                    return_list.append([nums[left], number, nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1    
                elif nums[left] + number + nums[right] > 0:
                    right -= 1
                else:
                    left += 1

        return return_list