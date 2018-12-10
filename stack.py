#!/usr/bin/python
class Stack:
    def __init__(self, stack_values):
        self.items = stack_values
    def is_empty(self):
        if self.items == []:
            return True
        else:
            return False
    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
s= Stack([34, 76, 87])
print s.is_empty()
i=s.push(98)
print i
print s.pop()
print s.peek()
