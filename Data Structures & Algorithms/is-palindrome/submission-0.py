class Solution:
    def isPalindrome(self, s: str) -> bool:
        sl=s.lower()
        # cleaned = "".join(char for char in text if char.isalnum())
        start=0
        end=len(sl)-1
        while end>start:
            if sl[end].isalnum()==False:
                end-=1
            elif sl[start].isalnum()==False:
                start+=1
            else:
                if sl[start]==sl[end]:
                    start+=1
                    end-=1
                else:
                    return False
        return True
