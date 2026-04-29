class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag={}
        for i in strs:
            key = "".join(sorted(i))
            if key in anag:
                anag[key].append(i)
            else:
                anag[key]=[i]
        return(list(anag.values()))