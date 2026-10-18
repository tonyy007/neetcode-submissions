class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0,0
        slow = nums[slow]
        fast = nums[fast]
        fast = nums[fast]
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            
        print(fast, slow)

        slow_2 = 0
        while slow != slow_2:
            slow_2 = nums[slow_2]
            slow = nums[slow]
        print(slow)

        return slow