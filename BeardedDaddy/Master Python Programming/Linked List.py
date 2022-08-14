class LinkedList(object):
    def__init__(self, head=None):
        self.head = head
    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter +=1
        return None
    
