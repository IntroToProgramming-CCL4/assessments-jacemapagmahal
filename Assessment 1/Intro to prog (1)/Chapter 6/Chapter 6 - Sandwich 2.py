sandwich_orders = ["tuna", "steak", "zinger", "pastrami", "veggie", "pastrami", "chicken"]

finished_sandwiches = []

print("Sorry, we've run out of pastrami.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_order = sandwich_orders.pop(0)
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

# Print the list of finished sandwiches
print("\nList of Finished Sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
