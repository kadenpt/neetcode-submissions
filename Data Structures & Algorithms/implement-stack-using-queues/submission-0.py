class MyStack:

    def __init__(self):
        self.main = deque()
        self.ph = deque()
        
    def push(self, x: int) -> None:
        self.ph.append(x)
        for _ in range(len(self.main)):
            self.ph.append(self.main.popleft())
        temp = self.ph
        self.ph = self.main
        self.main = temp
        
    def pop(self) -> int:
        return self.main.popleft()

    def top(self) -> int:
        return self.main[0]

    def empty(self) -> bool:
        return len(self.main) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()