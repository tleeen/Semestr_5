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

    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp


def rev_arr_iterative(arr):
    ab = None
    current = arr.head
    b = current.getNext()
    while b is not None:
        current.setNext(ab)
        ab = current
        current = b
        b = b.getNext()
    current.setNext(ab)
    arr.head = current
    return current


mylist = UnorderedList()
mylist.add(345)
mylist.add(346)
mylist.add(30045674)
mylist.add(2)
mylist.add(7)
mylist.add(900)
print(mylist)
rev_arr_iterative(mylist)
print(mylist)
