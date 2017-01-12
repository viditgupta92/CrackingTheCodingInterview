class node:
    def __init__(self):
        self.data = None
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = node()
        new_node.data = data
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node

    def remove(self):
        if self.head == None:
            return False
        else:
            item = self.head.data
            self.head = self.head.next
            return item

    def list_print(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

class Animal:
    def __init__(self,n):
        self.name = n
        self.order = 0

    def set_order(self, ord):
        self.order = ord

    def get_order(self):
        return self.order

class Dog(Animal):
    def __init__(self,n):
        super(Dog,self).__init__(n)

class Cat(Animal):
    def __init__(self,n):
        super(Cat,self).__init__(n)

class AnimalQueue:
    def __init__(self):
        self.dogs = linked_list()
        self.cats = linked_list()
        self.order = 0

    def enqueue(self, a):
        a.set_order(self.order)
        self.order += 1
        if isinstance(a,Dog):
            self.dogs.add_node(a)
        else:
            self.cats.add_node(a)

    def dequeueAny(self):
        if self.dogs.head == None:
            temp = self.dequeueCat()
        elif self.cats.head == None:
            temp = self.dequeueDog()
        else:
            d = self.dogs.head.data.order
            c = self.cats.head.data.order
            if d < c:
                temp = self.dequeueDog()
            else:
                temp = self.dequeueCat()
        return temp

    def dequeueDog(self):
        return self.dogs.remove().name

    def dequeueCat(self):
        return self.cats.remove().name

aq = AnimalQueue()
aq.enqueue(Cat('amy'))
aq.enqueue(Dog('stella'))
aq.enqueue(Dog('tommy'))
print(aq.dequeueAny())
print(aq.dequeueAny())
#print(aq.dequeueDog())
#print(aq.dequeueDog())
#print(aq.dequeueDog())




