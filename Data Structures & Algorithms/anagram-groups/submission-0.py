from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashes = [dict(Counter(w)) for w in strs]
        ans = defaultdict(list)

        for h in range(len(hashes)):
            ans[tuple(sorted(hashes[h].items()))].append(strs[h])

        return list(dict(ans).values())