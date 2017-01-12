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

class MyQueue(stack):

    def __init__(self):
        self.stack_oldest = stack()
        self.stack_newest = stack()

    def add(self,val):
        self.stack_newest.push(val)

    def shift_stacks(self):
        if self.stack_oldest.isEmpty() == True:
            while self.stack_newest.isEmpty() != True:
                self.stack_oldest.push(self.stack_newest.pop())

    def peek(self):
        self.shift_stacks()
        return self.stack_oldest.peek()

    def remove(self):
        self.shift_stacks()
        return self.stack_oldest.pop()

    def print_queue(self):
        self.shift_stacks()
        while self.stack_oldest.isEmpty() != True:
            print(self.stack_oldest.pop())

q = MyQueue()
q.add(1)
q.add(2)
q.add(3)
q.add(4)
print("Peek: ")
print(q.peek())
print("Remove: ")
print(q.remove())
print("Queue: ")
q.print_queue()