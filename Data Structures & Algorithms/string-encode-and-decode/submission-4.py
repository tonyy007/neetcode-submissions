class Solution:
    sep = ""
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "   "
        string = ""
        for word in strs:
            new = "".join(word)
            new = new.split(" ")
            for character in new:
                self.sep += character
        for word in strs:
            string += ("".join(word))
            string += " "
            string += self.sep
            string += " "
        
        return string
    def decode(self, s: str) -> List[str]:
        if s == "   ":
            return []
        result = s.split(" " + self.sep + " ")
        result.pop()
        return result
