from itertools import count


class MyHashableKey:
    def __init__(self, int_value, string_value):
        self.int_value = int_value
        self.string_value = string_value

    def __eq__(self, other):
        if self.int_value == other.int_value and self.string_value == other.string_value:
            return True
        return False

    def __hash__(self):
        hash = 0
        for char in self.string_value:
            value = ord(char) 
            if char == self.string_value[0]:
                value *= 13    
            hash += value * self.int_value * 53     
        return hash