# Python uses dictionaries to store key-value pairs
# From Python 3.7 upwards,
#  dicts are ordered
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


my_family_phones = {
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

print(my_family_phones["phone_two"])

print("Printing all the phones in the dictionary")
for phone in my_family_phones:
    print(my_family_phones[phone])


#declare a new dictionary]
wanted_phone= {
        "Brand": "Apple",
        "Make": "iPhone",
        "Version": "15 ProMax",
        "YoM": 2023,
        "Origin": "China"
}
print(f"My phone is an {wanted_phone['Make']} {wanted_phone['Version']}")
print(type(wanted_phone))
print(wanted_phone)

#dictionary is ordered, mutable unlike sets and tuples(which you have to recreate the structure)
#modifying the dictionary
wanted_phone= {
        "Brand": "Apple",
        "Make": "iPhone",
        "Version": "15 ProMax",
        "YoM": 2023,
        "Origin": "China"
}
wanted_phone["Version"]= "16 ProMax" #alter the wanted_phone dictionary
print(wanted_phone)

wanted_phone.pop("YoM") #remove an entry from the dictionary
print(wanted_phone)

#inspect the dictionary for existing key-values
if "Brand" in wanted_phone :
    print(f"The brand {wanted_phone["Brand"]} exists")
else :
    print("not available")

