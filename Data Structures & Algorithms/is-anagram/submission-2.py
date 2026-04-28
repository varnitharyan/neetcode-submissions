class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seens = {}
        seent = {}
        for i in s:
            if i in seens:
                seens[i]+=1
            else:
                seens[i]=1
        for i in t:
            if i in seent:
                seent[i]+=1
            else:
                seent[i]=1
        return seens==seent