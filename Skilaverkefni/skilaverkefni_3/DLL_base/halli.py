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
        if self.reverse() == True:
            node = self.tail.prev
        else:
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
        if self.current_position == position:
            return
        elif self.current_position > position:
            self.current_position -= 1
            self.current_node = self.current_node.prev
            self.move_to_pos(position)
        elif self.current_position < position:
            self.current_position += 1
            self.current_node = self.current_node.next
            self.move_to_pos(position)


    def sort(self):
        if self.head == None:
            return
        self.current_node = self.head
        self.sort_helper(self.current_node)
    
    
    def sort_helper(self, current_node):
        if current_node.next != None:
            index = self.current_node.next
            if index != None:
                if self.current_node.data > index.data:
                    temp = self.current_node.data
                    self.current_node.data = index.data
                    index.data = temp
                index = index.next
                current_node = current_node.next
                self.sort_helper(current_node)
        else:
            return

    def sort_recursion(self):
        pass

   