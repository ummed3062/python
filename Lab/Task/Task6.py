# Create a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# Access elements in a tuple
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Slicing a tuple
print("Slice from index 1 to 3:", my_tuple[1:4])

# Concatenating tuples
another_tuple = (6, 7, 8)
concatenated_tuple = my_tuple + another_tuple
print("Concatenated tuple:", concatenated_tuple)

# Check for element existence
print("Is 3 in the tuple?", 3 in my_tuple)

# Iterate through a tuple
print("Iterating through the tuple:")
for item in my_tuple:
    print(item)

# Length of a tuple
print("Length of tuple:", len(my_tuple))
