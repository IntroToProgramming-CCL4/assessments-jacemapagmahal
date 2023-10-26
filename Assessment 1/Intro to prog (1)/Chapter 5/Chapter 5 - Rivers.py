rivers = {
    "pasig": "philippines",
    "amazon": "brazil",
    "nile": "egypt"
    
    
}

for river, country in rivers.items():
    print(f"The {river.capitalize()} runs through {country.capitalize()}.")

print("\nList of Rivers:")
for river in rivers.keys():
    print(river.capitalize())

print("\nList of Countries:")
for country in rivers.values():
    print(country.capitalize())
