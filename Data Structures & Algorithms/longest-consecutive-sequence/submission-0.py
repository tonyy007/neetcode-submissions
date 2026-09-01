class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        nums = set(nums)
        for element in nums:
            count = 1
            if element - 1 in nums:
                continue
            else:
                check = element + 1
                while check in nums:
                    count += 1
                    check += 1

            length = max(count, length)

        return length