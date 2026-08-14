class MinStack:

    def __init__(self):
        self.st = []
        self.mn = 0

    def push(self, value: int) -> None:
        if not self.st:
            self.st.append(0)
            self.mn = value
        else:
            diff = value - self.mn
            self.st.append(diff)
            if diff < 0:
                self.mn = value

    def pop(self) -> None:
        diff = self.st.pop()
        if diff < 0:
            self.mn -= diff

    def top(self) -> int:
        diff = self.st[-1]
        if diff >= 0:
            return self.mn + diff
        else:
            return self.mn
    def getMin(self) -> int:
        return self.mn
