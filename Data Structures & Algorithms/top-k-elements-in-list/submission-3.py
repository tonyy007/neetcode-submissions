class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for i in range(len(nums) + 1)]

        hash = {}

        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1
        
        for num in hash:
            count[hash[num]].append(num)
        
        return_list = []
        
        for i in range(len(count) - 1,0,-1):
            if len(count[i]) == 0:
                continue
            for j in range(len(count[i])):
                return_list.append(count[i][j])
                if(len(return_list) == k):
                    return return_list
        return return_list