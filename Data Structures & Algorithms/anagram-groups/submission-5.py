class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = {}
        for i in strs:
            count = [0]*26
            for j in i:
                count[ord(j)-ord('a')]+=1
            if tuple(count) in anag:
                anag[tuple(count)].append(i)
            else:
                anag[tuple(count)]=[i]
        return(list(anag.values()))