"""
Lists are a collection of data
"""


my_list = [80, 96, 72, 100, 8]
print(my_list)
print(my_list[1]) # just like in JavaScript, the index prints the element in that index position

print(my_list[-1]) # the -1 index is the first element from the end

my_list[0] = 25 # just like in JS, this reassigns index 0
print(my_list)

print(len(my_list)) # this is Python way of finding length of array

print(my_list[0:2]) # Python way of slicing (prints 0, 1, up to but not including 2)

# INSERT AND DELETE

my_list.append(1000) # inserts 1000 at the end of array
print(my_list)

my_list.insert(2, 1000) # inserts at a specific index
print(my_list)

my_list.remove(8) # deletes the value from the array
print(my_list)

my_list.pop(0) # removes the value at index 0
print(my_list)

my_list.sort() # sorts numerically smallest to highest
print(my_list)









