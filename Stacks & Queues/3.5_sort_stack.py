class node:
    def __init__(self):
        self.data = None
        self.next = None


class stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        n = node()
        n.data = item
        n.next = self.top
        self.top = n

    def pop(self):
        if self.top == None:
            return 0
        else:
            item = self.top.data
            self.top = self.top.next
        return item

    def peek(self):
        if self.top == None:
            return 0
        else:
            return self.top.data

    def isEmpty(self):
        return self.top == None

    def print_stack(self):
        temp = self.top
        while temp != None:
            print(temp.data)
            temp = temp.next

    def sort_stack(self):
        s = stack()
        while self.top != None:
            t = self.pop()
            while s.peek() > t:
                self.push(s.pop())
            s.push(t)
        return s.print_stack()

s = stack()
s.push(2)
s.push(1)
s.push(4)
s.push(3)
s.sort_stack()