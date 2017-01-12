class node:
    def __init__(self):
        self.data = None
        self.next = None

class stack:
    def __init__(self):
        self.top = None

    def push(self,item):
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

class stack_with_min(stack):

    def __init__(self):
        self.s = stack()
        self.top = None

    def push(self,val):
        if val <= self.cal_min():
            self.s.push(val)
        super(stack_with_min,self).push(val)

    def pop(self):
        val = super(stack_with_min, self).pop()
        if val == self.cal_min():
            self.s.pop()
        return val

    def cal_min(self):
        if self.s.isEmpty() == True:
            return 10000
        else:
            return self.s.peek()

s1 = stack_with_min()
s1.push(5)
print("Stack: ")
s1.print_stack()
print("Min: ")
print(s1.cal_min())
s1.push(6)
print("Stack: ")
s1.print_stack()
print("Min: ")
print(s1.cal_min())
s1.push(3)
print("Stack: ")
s1.print_stack()
print("Min: ")
print(s1.cal_min())
s1.push(7)
print("Stack: ")
s1.print_stack()
print("Min: ")
print(s1.cal_min())
s1.pop()
print("Stack: ")
s1.print_stack()
print("Min: ")
print(s1.cal_min())
s1.pop()
print("Stack: ")
s1.print_stack()
print("Min: ")
print(s1.cal_min())



