# Supermarket Billing System

products = {
    "Rice": 60,
    "Sugar": 45,
    "Milk": 30,
    "Bread": 40,
    "Eggs": 6,
    "Oil": 150,
    "Soap": 35,
    "Shampoo": 120,
    "Biscuits": 20,
    "Tea": 180
}

cart = {}
customer_name = input("Enter Customer Name: ")

print("\n===========================================")
print("        WELCOME TO SMART MART")
print("      Visakhapatnam, Andhra Pradesh")
print("===========================================")

while True:

    print("\n----------- MENU -----------")
    print("1. View Products")
    print("2. Add Product to Cart")
    print("3. Generate Bill")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("\nAvailable Products")
        print("-------------------------------")
        print("Product\t\tPrice")
        print("-------------------------------")

        for item, price in products.items():
            print(item, "\t\t₹", price)

    elif choice == "2":

        product = input("Enter Product Name: ")

        if product in products:

            quantity = input("Enter Quantity: ")

            if quantity.isdigit():

                quantity = int(quantity)

                if quantity > 0:

                    if product in cart:
                        cart[product] += quantity
                    else:
                        cart[product] = quantity

                    print("Product Added Successfully!")

                else:
                    print("Quantity should be greater than 0.")

            else:
                print("Invalid Quantity! Enter numbers only.")

        else:
            print("Product Not Available.")

    elif choice == "3":

        if len(cart) == 0:
            print("\nCart is Empty!")
            continue

        print("\n")
        print("==============================================================")
        print("                    SMART MART")
        print("            Visakhapatnam, Andhra Pradesh")
        print("==============================================================")
        print("Customer Name :", customer_name)
        print("==============================================================")
        print("{:<15}{:<10}{:<12}{:<12}".format("Item", "Qty", "Price", "Total"))
        print("--------------------------------------------------------------")

        subtotal = 0

        for item, qty in cart.items():

            price = products[item]
            total = price * qty
            subtotal += total

            print("{:<15}{:<10}{:<12}{:<12}".format(item, qty, price, total))

        tax = subtotal * 0.12
        grand_total = subtotal + tax

        print("--------------------------------------------------------------")
        print("Subtotal : ₹", round(subtotal, 2))
        print("Tax (12%): ₹", round(tax, 2))
        print("Grand Total : ₹", round(grand_total, 2))
        print("==============================================================")
        print("        THANK YOU FOR SHOPPING WITH US!")
        print("            VISIT AGAIN!")
        print("==============================================================")

        break

    elif choice == "4":

        print("\nThank You for Visiting Smart Mart!")
        print("Have a Nice Day!")
        break

    else:
        print("Invalid Choice! Please Try Again.")