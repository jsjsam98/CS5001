class Stack:
    def __init__(self):
        self.data = list()
    def push(self, item):
        self.data.append(item)
    def pop(self):
        return self.data.pop()
mystack = Stack()
mystack.push(1)
mystack.push(2)
mystack.push(3)
mystack.push(4)
mystack.push(5)
mystack.pop()
mystack.pop()
mystack.pop()
print(mystack.data)