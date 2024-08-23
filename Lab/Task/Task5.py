# Create a list
my_list = [1, 2, 3]
print("Initial list:", my_list)

# Append an item to the list
my_list.append(4)
print("After appending 4:", my_list)

# Append multiple items to the list
my_list.extend([5, 6])
print("After appending 5 and 6:", my_list)

# Remove an item from the list by value
my_list.remove(2)
print("After removing 2:", my_list)

# Remove an item from the list by index
del my_list[0]  # Removes the first element
print("After removing the first element:", my_list)

# Clear the entire list
my_list.clear()
print("After clearing the list:", my_list)
