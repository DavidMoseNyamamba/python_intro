# Declare and initialize a list
fruits = ["Orange", "Peach", "Banana", "Mango", "Plum"]
print(fruits)

# Loop through entire list of fruits
for fruit in fruits:
    print(fruit)

# Retrieve list items
print(f"The fruit at position 1: {fruits[0]}")
print(f"The fruit at end of the list: {fruits[-1]}")

# Check length of the list
print(f"The fruit basket currently has {len(fruits)} fruits")

# Add something to the list
fruits.append("Lemon")
print(fruits)
# Check length of the list
print(f"The fruit basket currently has {len(fruits)} fruits")

# Add a list item to a specific position in the list
fruits.insert(2, "Apple")
print(fruits)

# Remove specific item from the list
fruits.remove("Lemon")
print(fruits)

# Remove item from a specified index on list
fruits.pop(0)
print(fruits)

# Remove item from the end of list
fruits.pop()
print(fruits)
