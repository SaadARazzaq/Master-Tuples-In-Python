import os
import time as t

print("\t\t***Python Program starting shortly...***")
t.sleep(1.5)

# There are various tuple methods in Python

# 1) count(): This method counts how many times a certain element has come in a tuple.
# There must be one argument passed to this method, and that argument must be present inside the tuple.

print("\n<---------------1) count() method---------------->\n")

count_tuple = (1, 2, 3, 4, 2, 1, 2, 3)
print("Tuple values are: ", count_tuple)

for i in range(4):
    print(f"Number of times {i+1} has come in tuple", end=": ")
    print(count_tuple.count(i+1))

# 2) index(): This is used to find out the location of a certain element in a given tuple.
# Returns the index of that element in the tuple.
# NOTE: The element you pass in the index() method must be present in the tuple.

t.sleep(3)
print("\n<---------------2) index() method---------------->\n")

tuple_index = ("apple", "banana", "orange", "banana", "grape")
print("Tuple has values: ", tuple_index)

var1 = tuple_index.index("apple")
print("Location of 'apple' in tuple is: ", var1)

var2 = tuple_index.index("banana")
print("Location of 'banana' in tuple is: ", var2)

# 3) len(): This method returns the length or the number of elements in the tuple.

t.sleep(3)
print("\n<---------------3) len() method---------------->\n")

len_tuple = (10, 20, 30, 40, 50)
print("Tuple values are: ", len_tuple)
print("Length of tuple is: ", len(len_tuple))

# 4) sorted(): This method returns a new sorted list from the elements of the tuple.

t.sleep(3)
print("\n<---------------4) sorted() method---------------->\n")

tuple_to_sort = (4, 2, 8, 1, 6)
print("Original tuple: ", tuple_to_sort)
sorted_tuple = tuple(sorted(tuple_to_sort))
print("Sorted tuple: ", sorted_tuple)

# 5) max() and min(): These methods return the maximum and minimum values in the tuple.

t.sleep(3)
print("\n<---------------5) max() and min() methods---------------->\n")

tuple_max_min = (14, 27, 5, 8, 42)
print("Tuple values are: ", tuple_max_min)
print("Maximum value in tuple: ", max(tuple_max_min))
print("Minimum value in tuple: ", min(tuple_max_min))

# 6) any() and all(): These methods return True if any or all elements in the tuple are True.

t.sleep(3)
print("\n<---------------6) any() and all() methods---------------->\n")

tuple_bool = (True, False, True, True)
print("Tuple values are: ", tuple_bool)
print("Any True in tuple: ", any(tuple_bool))
print("All True in tuple: ", all(tuple_bool))

# 7) tuple(): This method converts a iterable to a tuple.

t.sleep(3)
print("\n<---------------7) tuple() method---------------->\n")

list_to_convert = [1, 2, 3, 4]
print("Original list: ", list_to_convert)
converted_tuple = tuple(list_to_convert)
print("Converted tuple: ", converted_tuple)

# 8) reversed(): This method returns a reverse iterator of the tuple.

t.sleep(3)
print("\n<---------------8) reversed() method---------------->\n")

tuple_to_reverse = (1, 2, 3, 4, 5)
print("Original tuple: ", tuple_to_reverse)
reversed_tuple = tuple(reversed(tuple_to_reverse))
print("Reversed tuple: ", reversed_tuple)

# 9) slice [:]: This is not a method, but tuples support slicing to create new tuples with specific elements.

t.sleep(3)
print("\n<---------------9) Slicing a tuple---------------->\n")

original_tuple = (10, 20, 30, 40, 50)
print("Original tuple: ", original_tuple)

# Creating a new tuple with elements from index 1 to 3
sliced_tuple = original_tuple[1:4]
print("Sliced tuple: ", sliced_tuple)

# 10) + (Concatenation): Tuples support concatenation to combine two tuples into a new one.

t.sleep(3)
print("\n<---------------10) Concatenating tuples---------------->\n")

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print("Tuple 1: ", tuple1)
print("Tuple 2: ", tuple2)
print("Concatenated tuple: ", concatenated_tuple)

# 11) * (Repetition): Tuples support repetition to create a new tuple with repeated elements.

t.sleep(3)
print("\n<---------------11) Repeating a tuple---------------->\n")

original_tuple = (1, 2, 3)
repeated_tuple = original_tuple * 3
print("Original tuple: ", original_tuple)
print("Repeated tuple: ", repeated_tuple)

# 12) sorted() with key parameter: This method allows you to customize the sorting order using a key function.

t.sleep(3)
print("\n<---------------12) sorted() with key parameter---------------->\n")

tuple_to_sort = ((1, 4), (3, 2), (5, 1))
print("Original tuple: ", tuple_to_sort)

# Sorting based on the second element of each tuple
sorted_tuple = tuple(sorted(tuple_to_sort, key=lambda x: x[1]))
print("Sorted tuple based on the second element: ", sorted_tuple)

# 13) enumerate(): This function adds counter to an iterable and returns it as an enumerate object.

t.sleep(3)
print("\n<---------------13) enumerate() function---------------->\n")

tuple_to_enumerate = ('apple', 'banana', 'orange')
print("Original tuple: ", tuple_to_enumerate)

# Using enumerate to get both index and value
enumerated_tuple = tuple(enumerate(tuple_to_enumerate))
print("Enumerated tuple: ", enumerated_tuple)

# 14) zip(): This function returns an iterator of tuples, where the first item in each passed iterator is paired together.

t.sleep(3)
print("\n<---------------14) zip() function---------------->\n")

tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3)
zipped_tuple = tuple(zip(tuple1, tuple2))
print("Tuple 1: ", tuple1)
print("Tuple 2: ", tuple2)
print("Zipped tuple: ", zipped_tuple)

# 15) in and not in: These operators allow you to check if an element is present in a tuple.

t.sleep(3)
print("\n<---------------15) 'in' and 'not in' operators---------------->\n")

check_tuple = (10, 20, 30, 40, 50)
element_to_check = 30
print("Tuple: ", check_tuple)

# Checking if the element is present
print(f"{element_to_check} is {'in' if element_to_check in check_tuple else 'not in'} the tuple.")

# 16) Tuple Unpacking: This allows you to assign values of a tuple to variables.

t.sleep(3)
print("\n<---------------16) Tuple Unpacking---------------->\n")

tuple_to_unpack = (100, 200, 300)
a, b, c = tuple_to_unpack
print("Original tuple: ", tuple_to_unpack)
print("Unpacked values - a:", a, "b:", b, "c:", c)

# 17) map(): This function applies a given function to all the items in an input list (or tuple) and returns an iterator.

t.sleep(3)
print("\n<---------------17) map() function---------------->\n")

tuple_to_map = (1, 2, 3, 4, 5)
print("Original tuple: ", tuple_to_map)

# Using map to square each element in the tuple
squared_tuple = tuple(map(lambda x: x**2, tuple_to_map))
print("Squared tuple: ", squared_tuple)

# 18) filter(): This function filters the elements of a tuple based on a given function.

t.sleep(3)
print("\n<---------------18) filter() function---------------->\n")

tuple_to_filter = (10, 15, 20, 25, 30)
print("Original tuple: ", tuple_to_filter)

# Using filter to keep only even numbers in the tuple
filtered_tuple = tuple(filter(lambda x: x % 2 == 0, tuple_to_filter))
print("Filtered tuple (even numbers only): ", filtered_tuple)

# 19) reduce(): This function applies a rolling computation to sequential pairs of values in a tuple.

t.sleep(3)
print("\n<---------------19) reduce() function---------------->\n")

from functools import reduce

tuple_to_reduce = (1, 2, 3, 4, 5)
print("Original tuple: ", tuple_to_reduce)

# Using reduce to calculate the product of all elements in the tuple
product = reduce(lambda x, y: x * y, tuple_to_reduce)
print("Product of elements in the tuple: ", product)

# 20) Tuple as Keys in Dictionary: Tuples can be used as keys in dictionaries.

t.sleep(3)
print("\n<---------------20) Tuple as Keys in Dictionary---------------->\n")

tuple_as_key_dict = {(1, 2): 'apple', (3, 4): 'banana', (5, 6): 'orange'}
print("Dictionary with tuples as keys: ", tuple_as_key_dict)
