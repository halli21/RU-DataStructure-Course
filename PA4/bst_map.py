class ItemExistsException(Exception):
    pass

class NotFoundException(Exception):
    pass

class NotKeyExeption(Exception):
    pass

class NoValueExeption(Exception):
    pass

class BSTNode:
    def __init__(self, key=None, data=None, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BSTMap:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key, data):
        if key == None:
            raise NotKeyExeption
        if data == None:
            raise NoValueExeption
        self.root = self.insert_recur(self.root, key, data)


    def insert_recur(self, node, key, data):
        if node == None:
            self.size += 1
            return BSTNode(key, data)
        elif key < node.key:
            node.left = self.insert_recur(node.left, key, data)
        elif key > node.key:
            node.right = self.insert_recur(node.right, key, data)
        else:
            raise ItemExistsException
        return node


    def update(self, key, data):
        self.root = self.update_recur(self.root, key, data)


    def update_recur(self, node, key, data):
        if node == None:
            raise NotFoundException
        elif key < node.key:
            node.left = self.update_recur(node.left, key, data)
        elif key > node.key:
            node.right = self.update_recur(node.right, key, data)
        else:
            node.data = data
        return node

    def find(self, key):
        return self.find_recur(self.root, key)

    def find_recur(self, node, key):
        if node == None:
            raise NotFoundException
        elif key < node.key:
            return self.find_recur(node.left, key)
        elif key > node.key:
            return self.find_recur(node.right, key)
        else:
            return node.data

    def contains(self, key):
        return self.contains_recur(self.root, key)

    def contains_recur(self, node, key):
        if node == None:
            return False
        elif node.key == key:
            return True
        elif key < node.key:
            return self.contains_recur(node.left, key)
        elif key > node.key:
            return self.contains_recur(node.right, key)

    def __len__(self):
        return self.size


    def __str__(self):
        return "output: " + self.str_inorder(self.root)
       
    def str_inorder(self, node):
        if node == None:
            return ""
        return self.str_inorder(node.left,) + "{" +str(node.key) + ":" + str(node.data) + "} " + self.str_inorder(node.right)
        

    def remove(self, key):
        self.root = self.remove_recur(self.root, key)

    def remove_recur(self, node, key):
        if node == None:
            raise NotFoundException
        elif key < node.key:
            node.left = self.remove_recur(node.left, key)
        elif key > node.key:
            node.right =  self.remove_recur(node.right, key)
        else:
            return self.remove_node(node)

        return node

    def remove_node(self, node):
        if node.right == None and node.left == None:
            return None
        elif node.right == None:
            return node.left
        elif node.left == None:
            return node.right
        else:
            temp_node = self.remove_swap_left_most(node.right)
            node.key = temp_node.key
            node.data = temp_node.data
            node.right = self.remove_recur(node.right, temp_node.key)
            self.size -= 1
            return node

        
    def remove_swap_left_most(self, node):
        while node.left != None:
            node = node.left
        return node