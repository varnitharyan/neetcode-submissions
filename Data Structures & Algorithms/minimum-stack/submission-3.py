import sys
class MinStack:

    def __init__(self):
        self.a =[]
        self.minn = sys.maxsize
        # return a
        

    def push(self, val: int) -> None:
        self.a.append(val)
        self.minn=min(self.minn,val)

    def pop(self) -> None:
        if not self.a:
            return False
        else:
            poped = self.a.pop()
            if poped == self.minn:
                if self.a:
                    self.minn = min(self.a)
                else:
                    self.minn = sys.maxsize

    def top(self) -> int:
        return self.a[-1]

    def getMin(self) -> int:
        return self.minn 
