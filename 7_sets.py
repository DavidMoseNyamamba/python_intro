# Create and initialize a set
ea_cities = {"Kampala", "Nairobi", "Arusha", "Mombasa", "Nairobi"}

print(ea_cities)

print(f"There are {len(ea_cities)} cities in the set")

print(type(ea_cities))

ea_cities.add("Kigali")
print(ea_cities)

west_african_cities = {"Lagos", "Accra"}
south_african_cities = {"Cape Town", "Durban"}

master_city_list = {"New York"}

master_city_list.update(ea_cities)

print(master_city_list)
