class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        current = self.head
        count = 0
        while current is not None:
            if count == index:
                return current.value
            current = current.next
            count += 1
        return -1

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = self.head
        print(self.getValues())

    def insertTail(self, val: int) -> None:
        node = Node(val)
        if self.tail is not None:
            self.tail.next = node
        self.tail = node
        if self.head is None:
            self.head = self.tail
        print(self.getValues())

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        # handle head
        if index == 0:
            self.head = self.head.next
            print(self.getValues())
            return True
        current = self.head
        count = 1
        while current.next is not None:
            # remove current.next
            if count == index:
                # handle tail
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                print(self.getValues())
                return True
            count += 1
            current = current.next
        return False
        

    def getValues(self) -> List[int]:
        res = []
        current = self.head
        while current is not None:
            res.append(current.value)
            current = current.next
        return res
        
