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

    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

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


def move_to_front(n):
    a = UnorderedList()
    for i in range(n):
        string = input()
        if a.search(string):
            a.remove(string)
            a.add(string)
        else:
            a.add(string)
    print(a)


move_to_front(3)
