class MinStack:

    def __init__(self):
        self.a =[]
        # return a
        

    def push(self, val: int) -> None:
        self.a.append(val)
        # return a

    def pop(self) -> None:
        if not self.a:
            return False
        else:
            self.a.pop()
            # return a

    def top(self) -> int:
        return self.a[-1]

    def getMin(self) -> int:
        return min(self.a) 
