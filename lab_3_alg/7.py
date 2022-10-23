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
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
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

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


class Stack:
    def __init__(self):
        self.items = UnorderedList()

    def isEmpty(self):
        return self.items.isEmpty()

    def push(self, item):
        self.items.add(item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items.head.getData()

    def size(self):
        return self.items.size()

    def __str__(self):
        if self.items.head is None:
            return "[]"
        return self.items.__str__()


equation = Stack()
res = None
z = ["+", "-", "*", "/"]
while True:
    a = input()
    if a is not None:
        a = a.split()
        for i in a:
            if (i in z) and (equation.size() > 1):
                c1 = int(equation.pop())
                c2 = int(equation.pop())
                if i == "+":
                    res = c1 + c2
                elif i == "-":
                    res = c1 - c2
                elif i == "*":
                    res = c1 * c2
                elif i == "/":
                    res = c1 / c2
                equation.push(res)
                print(res)
                exit()
            elif i.isdigit():
                equation.push(i)
            else:
                print("Выражение составлено не корректно")
