class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.maxStack = []

    def push(self, x):
        self.stack.append(x)
        if not self.maxStack or x >= self.maxStack[-1]:
            self.maxStack.append(x)
            print(self.maxStack)

    def pop(self):
        if len(self.stack)>0:
            ele = self.stack.pop()
            if ele == self.maxStack[-1]:
                self.maxStack.pop()
            return ele
        else:
            return None

    def top(self):
        try:
            return self.stack[-1]
        except:
            None

    def peekMax(self):
        try:
            return self.maxStack[-1]
        except:
            None

    def popMax(self):
        if len(self.maxStack) > 0:
            while self.stack[-1] < self.maxStack[-1]:
                self.stack.pop()
            res=self.stack.pop()
            self.maxStack.pop()
            return res
        else:
            return None


mx = MaxStack()
mx.push(5)
mx.push(1)
mx.push(-5)


mx.popMax()
mx.popMax()
mx.top()