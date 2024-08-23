student = {                             # Creating a dictionary
    "name": "Ummed Singh",
    "sem": 5,
    "subject": "Python"
}

student1 = {
     "name": "Singh",
    "sem": 56,
}

print("Name:", student["name"])         # Accessing a value

student["subject"] = "Java"             # Modifying a value

student["company"] = "ByteXL"           # Adding a new key-value pair

print("Updated student record:", student) # Display updated dictionary

# Using dictionary methods
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Get method", student.get("name"))
print("Update Method", student.update(student1))
