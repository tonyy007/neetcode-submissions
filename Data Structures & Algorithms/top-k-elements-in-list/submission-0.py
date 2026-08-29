class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        from operator import itemgetter
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
        
        sorted_dict = dict(sorted(count.items(), key=itemgetter(1), reverse= True))
        most = []
        count = 0
        for key in sorted_dict:
            count += 1
            most.append(key)
            if count == k:
                break
        return most