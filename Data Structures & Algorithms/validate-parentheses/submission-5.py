class Solution:
    def isValid(self, s: str) -> bool:
        stact = []
        dictt={
            "}" : "{",
            "]" :  "[",
            ")" : "("
        }
        for sh in s:
            if sh in dictt.values():
                stact.append(sh)
            else:
                if not stact or stact[-1] != dictt[sh]:
                    return(False)
                stact.pop()
        return len(stact) == 0