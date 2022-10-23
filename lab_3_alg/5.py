class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def setPrev(self, newprev):
        self.prev = newprev


class DoubleList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head:
            return False
        return True

    def search(self, item):
        current = self.head
        a = False
        while current is not None and not a:
            if current.getData() == item:
                a = True
            else:
                current = current.getNext()
        return a

    def size(self):
        a = 0
        if self.head is None:
            return a
        current = self.head
        while current:
            a = a + 1
            current = current.getNext()
        return a

    def add(self, item):
        a = Node(item)
        a.setNext(self.head)
        if self.head:
            self.head.setPrev(a)
        self.head = a

    def append(self, item):
        current = self.head
        if current is None:
            self.add(item)
            return
        while current.getNext():
            current = current.getNext()
        a = Node(item)
        current.setNext(a)
        a.setPrev(current)

    def remove(self, item):
        current = self.head
        a = None
        b = False
        while not b:
            if current.getData() == item:
                b = True
            else:
                a = current
                current = current.getNext()
        if a is None:
            self.head = current.getNext()
        else:
            a.setNext(current.getNext())
        if current.getNext():
            current.getNext().setPrev(a)

    def pop(self, pos=None):
        current = self.head
        if pos is None:
            while current.getNext() is not None:
                current = current.getNext()
        else:
            for i in range(pos):
                current = current.getNext()
        self.remove(current.getData())
        return current.getData()

    def insert_after(self, pos, item):
        current = self.head
        for i in range(pos):
            current = current.getNext()
        a = Node(item)
        a.setNext(current.getNext())
        a.setPrev(current)
        if current.getNext():
            current.getNext().setPrev(a)
        current.setNext(a)

    def insert_before(self, pos, item):
        current = self.head
        for i in range(pos):
            current = current.getNext()
        a = Node(item)
        a.setNext(current)
        a.setPrev(current.getPrev())
        if current.getPrev():
            current.getPrev().setNext(a)
        current.setPrev(a)
        if a.getPrev() is None:
            self.head = a

    def __str__(self):
        a = "["
        current = self.head
        if current is None:
            return "[]"
        while True:
            a = a + str(current.getData())
            current = current.getNext()
            if current is None:
                break
            a = a + ", "
        return a + "]"


mylist = DoubleList()
print(mylist.isEmpty())
mylist.append(345635)
mylist.append(14567)
mylist.append(56)
mylist.append(6678)
mylist.append(34567465)
mylist.append(467456)
print(mylist.size())
print(mylist.search(56))
mylist.add(13)
print(mylist)
mylist.remove(56)
print(mylist)
mylist.pop(5)
print(mylist)
mylist.insert_before(3, 10)
print(mylist)
mylist.insert_after(0, 10)
print(mylist)

