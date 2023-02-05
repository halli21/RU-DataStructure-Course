class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.size = 0
        self.head = Node(None, None, None)
        self.tail = Node(None, self.head, None)
        self.head.next = self.tail
        self.current_node = self.tail
        self.current_position = 0

    def __str__(self):
        output_str = ""     
        node = self.head.next   
        while node != self.tail:  
            output_str += str(node.data) + " "
            node = node.next
        return output_str

    def __len__(self):
        return self.size

    def insert(self, value):
        n = Node(value, self.current_node.prev, self.current_node)
        self.current_node.prev.next = n
        self.current_node.prev = n
        self.current_node = n
        self.size += 1 

    def remove(self):
        if self.size == 0:
            return
        if self.current_node == self.tail:
            return
        self.current_node.prev.next = self.current_node.next
        self.current_node.next.prev = self.current_node.prev
        self.current_node = self.current_node.next
        self.size -= 1


    def get_value(self):
        return self.current_node.data

    def move_to_next(self):
        if self.tail != self.current_node:
            self.current_node = self.current_node.next
            self.current_position += 1

    def move_to_prev(self):
        if self.head.next != self.current_node:
            self.current_node = self.current_node.prev
            self.current_position -= 1

    def move_to_pos(self, position):
        if position < 0 or self.size < position:
            return None

        self.current_position = 0
        self.current_node = self.head.next

        while self.current_position != position:
            self.current_position += 1
            self.current_node = self.current_node.next


    def remove_all(self, value):
        left_node = self.head.next
        length = self.size
        
        for _ in range(length):
            if left_node.data == value:
                left_node.prev.next = left_node.next
                left_node.next.prev = left_node.prev
                self.size -= 1
            left_node = left_node.next
        
        if self.current_node.data == value:
            self.current_position = 0
            self.current_node = self.head.next


    def reverse(self):
        left_node = self.head.next
        right_node = self.tail.prev
        middle_index = self.size // 2

        for _ in range(middle_index):
            temp = left_node.data
            left_node.data = right_node.data
            right_node.data = temp
            left_node = left_node.next
            right_node = right_node.prev

        self.current_position = 0
        self.current_node = self.head.next
 

    def sort(self):
        left_node = self.head.next
        left_node_next = self.head.next.next

        for _ in range(self.size-1):
            for _ in range(self.size-1):
                if left_node_next.data == None:
                    break
                elif left_node.data > left_node_next.data:
                    temp = left_node.data
                    left_node.data = left_node_next.data
                    left_node_next.data = temp
                left_node_next = left_node_next.next
            left_node = left_node.next
            left_node_next = left_node.next

        self.current_position = 0
        self.current_node = self.head.next
