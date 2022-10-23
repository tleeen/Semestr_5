class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:

    def append(self, item):
        current = self.head
        if not current:
            self.head = Node(item)
            return
        while current.getNext():
            current = current.getNext()
        current.setNext(Node(item))

    def index(self, item):
        current = self.head
        a = False
        i = 0
        while (current is not None) and (not a):
            if current.getData() is item:
                a = True
            else:
                i += 1
                current = current.getNext()
        if not a:
            i = None
        return i

    def insert(self, pos, item):
        if pos == 0:
            self.add(item)
            return
        elif pos is self.size():
            self.append(item)
            return
        current = self.head
        for i in range(pos - 1):
            current = current.getNext()
        a = Node(item)
        a.setNext(current.getNext())
        current.setNext(a)

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

    def __str__(self):
        a = "["
        current = self.head
        while True:
            a = a + str(current.getData())
            current = current.getNext()
            if not current:
                break
            a = a + ", "
        return a + "]"

    def slice(self, start, stop):
        current = self.head
        i = 0
        a = UnorderedList()
        while i < start:
            i = i + 1
            current = current.getNext()
        a.head = Node(current.getData())
        b = a.head
        while start < (stop - 1):
            start = start + 1
            current = current.getNext()
            if not current:
                break
            c = Node(current.getData())
            b.setNext(c)
            b = b.getNext()
        b.setNext(None)
        return a

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


mylist = UnorderedList()
mylist.append(31)
mylist.append(77)
mylist.append(17)
mylist.append(93)
mylist.append(26)
mylist.append(54)

print(mylist)
print(mylist.index(54))
mylist.insert(3, 45)
print(mylist)
mylist.pop()
print(mylist)
mylist.pop(4)
print(mylist)
print(mylist.slice(1, 4))
