sandwich_orders = ["tuna", "steak", "zinger", "veggie", "chicken"]

finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop(0)
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

print("\nList of Finished Sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
