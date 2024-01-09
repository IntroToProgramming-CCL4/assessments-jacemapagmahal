import time

#Make a list of drinks and their name, price & quantity
drinks = [
    {
        'name':'Water',
        'price':10,
        'qty':10

    },
    {
        'name':'Cola',
        'price':12,
        'qty':10
    },
    {
        'name':'Iced Tea',
        'price':15,
        'qty':10
    },
    {   'name':'Coffee',
        'price':15,
        'qty':10
    },
    {   'name':'Sparkling Water',
        'price':18,
        'qty':10
    },
    {
        'name':'Juice',
        'price':15,
        'qty': 10
    }
]

#Make a list of snacks and their name, price & quantity
snacks = [
    {
        'name':'Sandwich',
        'price':18,
        'qty':10
    },
    {
        'name':'Footlong',
        'price':17,
        'qty':10
    },
    {
        'name':'Burger',
        'price':22,
        'qty':10
    },
    {
        'name':'Alfredo',
        'price':28,
        'qty':10
    },
    {   'name':'Steak',
        'price':40,
        'qty':10
    },
]

#Declare the variables

itemAvailable = False
stk = 0
stk2 = 0
price2 = 0
price = 0
total = 0
change = 0
typeOfOrder = ""
type = ""


#Make the menu
print("*********** Memento Grill ****************")
print("--------------- Menu ---------------------")


#Make a program that will illustrate to the user the menus of drinks & snacks
def getSnacks():
    print("\nSnacks")
    for item in range(len(snacks)):
        print(str(item + 1) + ". " + str(snacks[item]["name"]) + " " + str(snacks[item]["price"]) +"$")

def getDrinks():
    print("\nDrinks")
    for item in range(len(drinks)):
        print(str(item + 1) + ". " + str(drinks[item]["name"]) + " "+ str(drinks[item]["price"]) + "$")

getSnacks()
getDrinks()

print("\n")

#Make a program that will ask the user to input their order
while itemAvailable == False:
    order = str(input("Enter your order: "))
    for items in range(len(snacks)):
        if snacks[items]["name"] == order:
            typeOfOrder = snacks
            itemAvailable = True
            break

    for items in range(len(drinks)):
        if drinks[items]["name"] == order:
            typeOfOrder = drinks
            itemAvailable = True
            break
    if itemAvailable == False:
        print("Order doesn't exist")


#Make a program that will show the name, price & quantity of item
if itemAvailable:
    for items in range(len(typeOfOrder)):
        if typeOfOrder[items]["name"] == order:
            stk = typeOfOrder[items]["qty"]
            price = typeOfOrder[items]["price"]
            break

    print(str(stk) + " available item/s")


    qty = int(input("Enter quantity to buy: "))

 #Make a program that will tell the user there is insufficient item
    while qty > stk:
        print("Insufficent item. There is only " + str(stk) + " available item/s")
        qty = int(input("Enter quantity to buy: "))


    if (typeOfOrder == drinks):
        addons = "Snacks"
    else:
        addons = "Drinks"


#Make a program that will ask the user that they will add another order
    wantAddOns = str(input("Would you like to add " + str(addons) + "? Y/N: "))
    print("\n")

    if wantAddOns == "Y":
        print("\n")
        type2 = ""
        if (addons == "Snacks"):
            getSnacks()
            type2 = snacks
        else:
            getDrinks()
            type2 = drinks

        itemAvailable = False
        while itemAvailable == False:
            order2 = str(input("Enter your order: "))
            for items in range(len(type2)):
                if type2[items]["name"] == order2:
                    stk2 = type2[items]["qty"]
                    price2 = type2[items]["price"]
                    itemAvailable = True
                    break

            if itemAvailable == False:
                print("Order doesn't exist")

        print(str(stk2) + " available item/s")

        qty2 = int(input("Enter quantity to buy: "))

        while qty2 > stk2:
            print("Insufficent item. There is only " + str(stk) + " available item/s")
            qty2 = int(input("Enter quantity to buy: "))

 #Make a program that will review your order
        print("\nPlease review your order!!!\n")
        print("Snacks: " + str(qty) + " " + order)
        print("Drinks: " + str(qty2) + " " + order2)
        total = (qty * price) + (qty2 * price2)

        print("Amount to pay: " + str(total) + "$")


#Make a program that will ask the user to proceed or cancel the payment
        proceed = str(input("\nProceed to your payment or cancel your order? Y/N: "))

        if proceed == "Y":
            cash = int(input("Enter your money: "))


            while cash < total:
                cash = int(input("Not enough balance. \nPlease enter your money again: "))

            print("\n" + "----------- " +  order + " has been received." + " ----------------")
            change = cash - total

 #Make a program that will ask the user if they want a receipt
            wantRcpt = str(input("Do you want a receipt? Y/N: "))
            if wantRcpt == "Y":
                x = 3
                while x > 0:
                    print("----------- " + "Please wait... " + str(x) + " ----------------")
                    time.sleep(1)
                    x -= 1

                print("\n \n")
                print("----------- " + "Receipt"  + " ----------------")
                print("Snack: " + order)
                print("Quantity: " + str(qty))
                print("Drinks: " + order2)
                print("Quantity: " + str(qty2))
                print("Total Amount to pay: " + str(total)  + "$")
                print("Total Cash: " + str(cash)  + "$")
                print("Change: " + str(change) + "$")
                print("----------- " + "Thank you come again!!!"  + " ----------------")

            elif wantRcpt == "N":
                print("Change: " + str(change) + "$")
                print("----------- " + "Thank you come again!!!"  + " ----------------")
            else:
                print("Change: " + str(change) + "$")
                print("----------- " + "Thank you come again!!!"  + " ----------------")

        else:
            print("Cancel Order Successfully.")

    else:
        type = ""
        print("\nPlease review your order!!!\n")
        if typeOfOrder == drinks:
            print("Drinks: " + order)
            type = "Drinks"
        else:
            type = "Snacks"
            print("Snacks: " + order)

        print("Qty: " + str(qty))
        total = price * qty
        print("Total amount to pay: " + str(total) + "$")

        proceed = str(input("\nProceed to your payment or cancel your order? Y/N: "))

        if proceed == "Y":
            cash = int(input("Enter your money: "))

#Make a program that will tell the user that there is not enough balance
            while cash < total:
                cash = int(input("Not enough balance. \nPlease enter your money again: "))

            print("\n" + "----------- " +  order + " has been received." + " ----------------")
            change = cash - total

            wantRcpt = str(input("Do you want a receipt? Y/N: "))

            if wantRcpt == "Y":
                x = 3
                while x > 0:
                    print("----------- " + "Please wait... " + str(x) + " ----------------")
                    time.sleep(1)
                    x -= 1

                print("\n \n")
                print("----------- " + "Receipt"  + " ----------------")
#Make a program that will show the quantity, total  amount to pay, total cash & change
                print(type + ": " + order)
                print("Quantity: " + str(qty))
                print("Total Amount to pay: " + str(total)  + "$")
                print("Total Cash: " + str(cash)  + "$")
                print("Change: " + str(change) + "$")
                print("----------- " + "Thank you come again!!!"  + " ----------------")

            elif wantRcpt == "N":
                print("Change: " + str(change) + "$")
                print("----------- " + "Thank you come again!!!"  + " ----------------")
            else:
                print("Change: " + str(change) + "$")
                print("----------- " + "Thank you come again!!!"  + " ----------------")

        else:
            print("Cancel Order Successfully.")