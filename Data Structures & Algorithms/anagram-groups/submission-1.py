from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = defaultdict(list)

        for s in strs:
            hash = "".join(sorted(s))
            ans[hash].append(s)

        return list(dict(ans).values())