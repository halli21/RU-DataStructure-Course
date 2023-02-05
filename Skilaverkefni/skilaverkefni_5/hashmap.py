from bucket_map import *

class HashMap:
    def __init__(self, key=None, data=None, next=None):
        self.key = key
        self.data = data
        self.next = next
        self.capacity = 10
        self.lis = [0] * self.capacity

    
    def blehash(self, value):
        result = 0
        for character in value:
            result += ord(character) * 17
        return result

    def insert(self, key, data):
        h = hash(data)
        index = h % self.capacity
        bucket = self.lis[index]
        bucket.insert(key, data)

    def update(self, key, data):
        pass

    def find(self, key):
        pass

    def contains(self, key):
        pass

    def remove(self, key):
        pass

    def __setitem__(self, key, data):
        pass

    def __getitem__(self, key):
        pass

    def __len__(self):
        pass

    def rebuild(self):
        pass


def hash(value):
        result = 0
        for character in value:
            result += ord(character) * 17
        return result


h = hash("typpi")
print(h)
h = h % 10
print(h)