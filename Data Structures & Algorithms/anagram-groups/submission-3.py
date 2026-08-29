class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = defaultdict(list)
        
        for i in range(len(strs)):
            characters = [0] * 26
            for c in strs[i]:
                characters[ord(c) - ord("a")] += 1
            
            check[tuple(characters)].append(strs[i])
        #print(check)
        to_list = []
        for key in check:
            to_list.append(check[key])
        return to_list
