class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass

class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.size = 0

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        return_string = ""
        for i in range(self.size):
            return_string += str(self.arr[i])
            if i != self.size -1:
                return_string += ", "
        return return_string

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        self.insert(value, 0)

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        if index < 0 or index > self.size:
            raise IndexOutOfBounds()
        self.resize()
        for i in range(self.size, index, -1):
            self.arr[i] = self.arr[i-1]
        self.arr[index] = value
        self.size += 1

    #Time complexity: O(1) - constant time
    def append(self, value):
        self.resize()
        self.arr[self.size] = value
        self.size += 1

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        if index < 0 or index > self.size-1:
            raise IndexOutOfBounds()
        self.arr[index] = value

    #Time complexity: O(1) - constant time
    def get_first(self):
        value = self.arr[0]
        if value == None:
            raise Empty()
        return value

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        if index == None:
            raise NotFound()
        if index < 0 or index > self.size-1:
            raise IndexOutOfBounds()
        value = self.arr[index]
        return value

    #Time complexity: O(1) - constant time
    def get_last(self):
        value = self.arr[self.size-1]
        if value == None:
            raise Empty()
        return value

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        if self.size == self.capacity:
            self.capacity *= 2
            temp = [None] * self.capacity
            for i in range(self.size):
                temp[i] = self.arr[i]
            self.arr = temp

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        if index < 0 or index > self.size-1:
            raise IndexOutOfBounds()
        for i in range(index, self.size-1):
            self.arr[i] = self.arr[i+1]
        self.size -= 1
        self.arr[self.size] = None


    #Time complexity: O(1) - constant time
    def clear(self):
        self.arr = [None] * self.capacity
        self.size = 0

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        if True == self.check_if_not_ordered():
            raise NotOrdered()
        self.resize()
        for i in range(self.size, 0, -1):
            if self.arr[i-1] <= value:
                self.arr[i] = value
                self.size += 1
                return
            else:
                self.arr[i] = self.arr[i-1]
        
        self.arr[0] = value
        self.size += 1

    def check_if_not_ordered(self):
        self.resize()
        for i in range(self.size):
            if self.arr[i+1] != None and self.arr[i] > self.arr[i+1]:
                return True
                

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        low = 0
        high = self.size - 1
        if True == self.check_if_not_ordered():
            #linear search
            return self.linear_search(value)
        else:
            #binary searh
            return self.binary_search(value, low, high)


    def binary_search(self, value, low, high):
        if low > high:
            raise NotFound()
        mid = (low + high) // 2
        if self.arr[mid] == value:
            return mid 
        elif self.arr[mid] > value:
            return self.binary_search(value, low, mid - 1)
        elif self.arr[mid] < value:
            return self.binary_search(value, mid + 1, high)
    

    def linear_search(self, value, ins=0):
        if self.size < ins:
            raise NotFound()
        if value == self.arr[ins]:
            return ins
        return self.linear_search(value, ins+1)
        

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        index = self.linear_search(value)
        return self.remove_at(index)
  


if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_lis = ArrayList()
    arr_lis.append(1)
    arr_lis.append(2)
    arr_lis.append(3)
    arr_lis.append(4)
    arr_lis.remove_value(1)
    print(str(arr_lis))