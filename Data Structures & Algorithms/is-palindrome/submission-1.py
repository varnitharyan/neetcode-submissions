class Solution:
    def isPalindrome(self, s: str) -> bool:
        # sl=s.lower()
        # cleaned = "".join(char for char in text if char.isalnum())
        start=0
        end=len(s)-1
        while end>start:
            if s[end].isalnum()==False:
                end-=1
            elif s[start].isalnum()==False:
                start+=1
            else:
                if s[start].lower()==s[end].lower():
                    start+=1
                    end-=1
                else:
                    return False
        return True
