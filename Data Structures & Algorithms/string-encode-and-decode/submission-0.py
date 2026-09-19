class Solution:

    delimiter = "$^"

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += ((str(len(s))) + self.delimiter + s)
        return ans
    def decode(self, s: str) -> List[str]:
        c = 0
        ans = []
        while c < len(s):
            word_len = ""
            while s[c].isdigit():
                word_len += s[c]
                c += 1
            c += len(self.delimiter)
            ans.append(s[c:c+int(word_len)])
            c += int(word_len)
        
        return ans