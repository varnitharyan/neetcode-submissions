class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = {}

        for word in strs:
            count = [0] * 26
            
            for c in word:
                count[ord(c) - ord('a')] += 1
            
            key = tuple(count)  # hashable
            
            if key in anag:
                anag[key].append(word)
            else:
                anag[key] = [word]

        return list(anag.values())