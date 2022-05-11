class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SlinkedList:
    def __init__(self):
        self.headval = None


list1 = SlinkedList()
list1.headval = Node("Mon")  # type: ignore
e2 = Node("Tue")
e3 = Node("Wed")
#Link first Node to second node
list1.headval.nextval = end2


