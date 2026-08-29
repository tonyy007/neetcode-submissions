class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = dict()
        for i in range(len(strs)):
            sorted_word = "".join(sorted(strs[i]))
            if sorted_word in check:
                check[sorted_word].append(i)
            else:
                check[sorted_word] = [i]
        to_list = []

        for key in check:
            append_list = []
            for num in check[key]:
                append_list.append(strs[num])
            to_list.append(append_list)
        return to_list
