from hash_key import *


class ItemExistsException(Exception):
    pass

class NotFoundException(Exception):
    pass

class NotKeyExeption(Exception):
    pass



class BucketMap:
    def __init__(self, key=None, data=None, next=None):
        self.key = key
        self.data = data
        self.next = next

class Bucket:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, key, data):
        if key == None:
            raise NotKeyExeption
        self.head = self.insert_recur(self.head, key, data)


    def insert_recur(self, head, key, data):
        if head == None:
            self.size += 1
            return BucketMap(key, data)
        elif head.key == key:
            raise ItemExistsException
        else: 
            head.next = self.insert_recur(head.next, key, data)
        return head


    def update(self, key, data):
        if key == None:
            raise NotKeyExeption
        self.head = self.update_recur(self.head, key, data)


    def update_recur(self, head, key, data):
        if head == None:
            raise NotFoundException     
        elif key == head.key:
            head.data = data
        else:
            head.next = self.update_recur(head.next, key, data)
        return head

    def find(self, key):
        if key == None:
            raise NotKeyExeption
        return self.find_recur(self.head, key)

    def find_recur(self, head, key):
        if head == None:
            raise NotFoundException
        elif key == head.key:
            return head.data

        else:
            return self.find_recur(head.next, key)

    def contains(self, key):
        if key == None:
            raise NotKeyExeption
        return self.contains_recur(self.head, key)

    def contains_recur(self, head, key):
        if head == None:
            return False
        elif head.key == key:
            return True
        elif key > head.key:
            return self.contains_recur(head.next, key)

    def __len__(self):
        return self.size


    def __str__(self):
        return "output: " + self.str_inorder(self.head)
       
    def str_inorder(self, head):
        if head == None:
            return ""
        return "{" +str(head.key) + ":" + str(head.data) + "} " + self.str_inorder(head.next)
        

    def remove(self, key):
        if key == None:
            raise NotKeyExeption
        self.head = self.remove_recur(self.head, key)

    def remove_recur(self, head, key):
        if head == None:
            raise NotFoundException
        elif key == head.key:
            return self.remove_node(head)
        else:
            head.next =  self.remove_recur(head.next, key)
        return head

    def remove_node(self, head):
        if head.next == None:
            return None
        else:
            temp_node = self.remove_swap_left_most(head.next)
            head.key = temp_node.key
            head.data = temp_node.data
            head.next = self.remove_recur(head.next, temp_node.key)
            self.size -= 1
            return head

        
    def remove_swap_left_most(self, head):
        while head.next != None:
            head = head.next
        return head


    def __setitem__(self, key, data):
        if key == None:
            raise NotKeyExeption
        if self.contains(key):
            self.update(key, data)
        else:
            self.insert(key, data)


    def __getitem__(self, key):
        if key == None:
            raise NotKeyExeption
        return self.find(key)




class HashMap:
    def __init__(self):
        self.capacity = 10
        self.lis = [None] * self.capacity
        self.size = 0

    def rebuild(self):
        true_max = self.capacity * 1.2
        if self.size == true_max:
            self.capacity *= 2
            temp = [None] * self.capacity
            for bucket in self.lis:
                if bucket != None:
                    n = bucket.head
                    while n != None:
                        h = hash(n.key)
                        index = h % self.capacity
                        b2 = Bucket()
                        if temp[index] is not None:
                            b2 = temp[index]
                        b2.insert(n.key, n.data)
                        temp[index] = b2
                        n = n.next
            self.lis = temp


    def insert(self, key, data):
        self.rebuild()
        h = hash(key)
        index = h % self.capacity
        b = Bucket()
        if self.lis[index] is not None:
            b = self.lis[index]
        b.insert(key, data) 
        self.lis[index] = b
        self.size += 1

    def update(self, key, data):
        h = hash(key)
        index = h % self.capacity
        b = Bucket()
        if self.lis[index] is  None:
            raise NotFoundException
        b = self.lis[index]
        b.update(key, data) 
        self.lis[index] = b

    def find(self, key):
        h = hash(key)
        index = h % self.capacity
        b = Bucket()
        if self.lis[index] is  None:
            raise NotFoundException
        b = self.lis[index]
        return b.find(key) 

    def contains(self, key):
        h = hash(key)
        index = h % self.capacity
        b = Bucket()
        if self.lis[index] is  None:
            return False
        b = self.lis[index]
        return b.contains(key)

    def remove(self, key):
        h = hash(key)
        index = h % self.capacity
        b = Bucket()
        if self.lis[index] is  None:
            raise NotFoundException
        b = self.lis[index]
        b.remove(key)

    def __setitem__(self, key, data):
        if key == None:
            raise NotKeyExeption
        if self.contains(key):
            self.update(key, data)
        else:
            self.insert(key, data)

    def __getitem__(self, key):
        if key == None:
            raise NotKeyExeption
        return self.find(key)

    def __len__(self):
        return self.size



h = HashMap()
h.insert(1, "word")
h.insert(500, "word1")
h.insert(40, "word2")
h.insert(4, "word3")
h.insert(5, "word5")
h.insert(200, "word")
h.insert(600, "word1")
h.insert(7, "word2")
h.insert(0, "word3")
h.insert(9, "word5")
h.insert(10, "word3")
h.insert(6, "word5")
h.insert(14, "word2")
h.insert(13, "word3")
h.insert(60, "word5")
h.insert(601, "word3")
h.insert(203, "word5")