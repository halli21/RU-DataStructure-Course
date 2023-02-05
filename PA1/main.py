class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass



def modulus(value_1, value_2):
    if value_1 < value_2:
        return value_1
    if value_1 == value_2:
        return 0
    return modulus(value_1-value_2, value_2)

print("modulus dæmi\n")
print(modulus(13, 4)) #1
print(modulus(12, 3)) #0
print(modulus(14, 3)) #2
    


def how_many(lis_1, lis_2, count=0):
    if len(lis_1) == 0:
        return count
    count = count_instances(lis_2, lis_1[0])
    return count + how_many(lis_1[1:], lis_2)


def count_instances(list, value):
    if len(list) == 0:
        return 0
    ret_val = count_instances(list[1:], value)
    if list[0] == value:
        ret_val += 1
    return ret_val


print("\n\n" + 100*"-" + "\n\n")
print("how many dæmi\n")



lis_1 = ["a","b","f","g","a","t","c"]
lis_2 =["a","b","c","d","e"]

print(how_many(lis_1, lis_2)) #4

lis_3 = ["a","f","d","t"]
lis_4 = ["a","b","c","d","e"]
print(how_many(lis_3, lis_4))  #2


print("\n\n" + 100*"-" + "\n\n")
print("remove dæmi\n")



lis_1 = ["a","b","f","g","a","t","c"]
size = 7
def remove_value(lis, value):
    index = linear_search(lis, 0, size-1, value)
    if index:
        lis = remove_at(lis, index, size)
        print(lis)
    else:
        raise NotFound()
    

def remove_at(lis, index, size):
    if index < 0 or index > size-1:
        raise IndexOutOfBounds()
    for i in range(index, size-1):
        lis[i] = lis[i+1]
    size -= 1
    lis[size] = None
    return lis


def ass_linear_search(lis, check_low, check_high, value):
    if check_high < check_low:
        return False
    if lis[check_low] == value:
        return check_low
    if lis[check_high] == value:
        return check_high
    return ass_linear_search(lis, check_low+1, check_high-1, value)
 

#print(remove_value(lis_1, "c"))


lis_1 = ["a","b","f","g","a","t","c"]
size = 7

def linear_search(lis, value, i=0):
    if size < i:
        print("ekki fundið")
    if value == lis[i]:
        return i
    return linear_search(lis, value, i+1)



print(linear_search(lis_1, "g"))