while True:
    age = input("Please enter your age: ")

    age = int(age)

    if age < 3:
        print("Your ticket is free.")
    elif 3 <= age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")
    break