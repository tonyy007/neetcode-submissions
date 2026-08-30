class Solution:

    def encode(self, strs: List[str]) -> str:
        itch = ""
        for word in strs:
            length = len(word)
            code = str(length) + "!"
            combined = code + word
            itch += combined
        
        return itch
    def decode(self, s: str) -> List[str]:
        string_list = []
        length = ""
        i = 0
        while i < len(s):
            if s[i] == "!":
                get = s[i+ 1: i + int(length) + 1]
                string_list.append(get)
                i = i + int(length) + 1
                length = ""
            else:
                length += s[i]
                i += 1
        return string_list
