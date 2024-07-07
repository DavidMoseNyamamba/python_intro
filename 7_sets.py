# Create and initialize a set
ea_cities = {"Kampala", "Nairobi", "Arusha", "Mombasa", "Nairobi"}

print(ea_cities)

print(f"There are {len(ea_cities)} cities in the set")

print(type(ea_cities))

ea_cities.add("Kigali")
print(ea_cities)

#append cities in west africa
west_african_cities = {"Lagos", "Accra"}
west_african_cities.update(ea_cities)
print(west_african_cities)

#append cities in south africa
south_african_cities = {"Cape Town", "Durban"}
south_african_cities.update(ea_cities)
print(south_african_cities)

#append cities in master city list
master_city_list = {"New York"}
master_city_list.update(ea_cities)
print(master_city_list)
