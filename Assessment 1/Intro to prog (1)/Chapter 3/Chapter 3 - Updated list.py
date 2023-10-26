guests = ["Gab", "Michael Jordan", "Kobe"]
for guest in guests:
    print(f"Dear {guest},")
    print("You are invited to dinner at my place. It will be an honor to have you as my guest!")

Cancelled = "Michael Jordan"

print(f"Unfortunately, Michael Jordan can't make it to dinner.\n")
new_guest = "Olsen"
guests[guests.index(Cancelled)] = new_guest

print("Updated Invitations:")
for guest in guests:
    print(f"Dear {guest},")
    print("You are invited to dinner at my place. It will be an honor to have you as my guest!\n")

