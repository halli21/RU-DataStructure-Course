class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def push_front(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node

        elif self.tail is None:
            self.tail = self.head
            self.tail.next = None
            self.head = node
            node.next = self.tail
        else:
            node.next = self.head
            self.head = node
        
        self.size += 1
    
    def pop_front(self):
        if self.head == None:
            return None
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data
    
    def push_back(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        elif self.tail == None:
            self.tail = node
            self.head.next = node
        else:
            self.tail.next = node
            self.tail = node
    
        self.size += 1

        

    def pop_back(self):
        if self.head == None:
            return None
        elif self.head.next == None:
            data = self.head.data
            self.head = None
            self.size -= 1
            return data
        elif self.head.next == self.tail:
            data = self.tail.data
            self.tail = None
            self.head.next = None
            self.size -= 1
            return data

        n = self.head
        while n.next != None:
            if n.next.next == None:
                data = n.next.data
                self.tail = n.next
                n.next = None
                self.size -= 1
                return data
            n = n.next


    def get_size(self):
        return self.size

    def __str__(self):
        n = self.head
        output = ""
        while True:
            if n == None:
                return output
            output += str(n.data) + " "
            n = n.next
