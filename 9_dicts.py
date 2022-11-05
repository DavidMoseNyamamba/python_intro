# Python uses dictionaries to store key-value pairs
# From Python 3.7 upwards, dicts are ordered
# In earlier versions, dictionaries were unordered
# Dicts don't allow duplicate values
# Dicts are changeable
# Dicts implement curly braces


# Declaring a dictionary
my_phone = {
    "Brand": "Samsung",
    "Make": "Galaxy",
    "Model": "S22",
    "YoM": 2022,
    "Origin": "South Korea"
}


print(my_phone)

print(f"My phone is a {my_phone['Brand']}")
print(f'My phone is a {my_phone["Brand"]} {my_phone["Model"]}')


my_phones = {
    "phone_one": {
        "Brand": "Samsung",
        "Make": "Galaxy",
        "Model": "S22",
        "YoM": 2022,
        "Origin": "South Korea"
    },

    "phone_two": {
        "Brand": "Apple",
        "Make": "iPhone",
        "Version": "13",
        "YoM": 2021,
        "Orign": "USA"
    },

    "phone_three": {
        "Brand": "Google",
        "Make": "Pixel",
        "Version": "6 Pro",
        "YoM": 2021,
        "Orign": "USA"
    }
}

print(my_phones["phone_two"])

print("Printing all the phones in the dictionary")
for phone in my_phones:
    print(my_phones[phone])
