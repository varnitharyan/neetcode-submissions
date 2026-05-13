class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        for i in s:
            if i == '(' or i == "{" or i == "[":
                a.append(i)
                continue
            if a:
                if i == ")" and  a[len(a)-1] == "(":
                    a.pop()
                elif i == "]" and a[len(a)-1] == "[":
                    a.pop()
                elif i == "}" and a[len(a)-1] == "{":
                    a.pop()
                else:
                    return(False)
            else:
                if s:
                    return(False)
        if not a:
            return(True)
        return(False)