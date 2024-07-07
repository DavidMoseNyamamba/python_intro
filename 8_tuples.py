# A structure that stores multiple values in one variable
# A tuple is unchangeable (immutable)
# A tuple is ordered
# A tuple is declared in rounded brackets

# Declare and initialize a tuple
my_cars = ("BWM", "Toyota", "Honda")
print(my_cars)

# Retrieve first item in tuple
print(my_cars[0])

# Check the length of the tuple
print(len(my_cars))

# # Add value to tuple
# my_cars[1] = "Mazda"
# my_cars[5] = "Nissan"

print(my_cars)



car_tuple = ("BWM", "Toyota", "Honda",25, "RollsRoyce")
print(car_tuple[-1]) #get last item
print(type(car_tuple)) #get type of structure

print(car_tuple.__len__()) #get length of tuple

#car_tuple[1] = "Merc"              #proof that you cannot change an existing tuple directly
#new_car_tuple = tuple(car_tuple)   
#print(car_tuple)
#print(new_car_tuple)

#add an item to tuple with list mechanism
my_cars= ("Suzuki" ,) + my_cars[1:]
print(my_cars)

#cast the tuple to a list
my_cars_list=list(my_cars)
my_cars_list[2]= "Porsche" #change the last item in the list
print(my_cars_list)

#convert back to list
new_car_tuple=tuple(my_cars_list)
print(new_car_tuple)
                    







