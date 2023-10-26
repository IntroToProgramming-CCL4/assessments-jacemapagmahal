print("Enter pizza toppings. Type 'exit' to exit.")

toppings = []

while True:
    topping = input("Enter a topping: ").lower()
    
    if topping == 'quit':
        break
    
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

print("Your pizza toppings:")
print(", ".join(toppings))
