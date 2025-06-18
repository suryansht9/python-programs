def take_order(menu_name, menu):
    print(f"\nHere is our {menu_name} menu:")
    for num, (item, price) in menu.items():
        print(f"{num}. {item} - ₹{price}")

    total = 0
    while True:
        order = input("\nEnter the number of the item you'd like to order (or 'q' to finish this meal): ")
        if order.lower() == 'q':
            break
        if order not in menu:
            print("Invalid item number. Please try again.")
            continue

        try:
            quantity = int(input(f"How many plates of {menu[order][0]} would you like? "))
            if quantity <= 0:
                print("Please enter a positive quantity.")
                continue
            item_total = quantity * menu[order][1]
            print(f"You ordered {quantity} x {menu[order][0]} = ₹{item_total}")
            total += item_total
        except ValueError:
            print("Please enter a valid number for quantity.")

    # ✅ After ordering ends
    print(f"\nYour total amount is ₹{total}")

    # Ask for confirmation
    call = input("Sir/Mam, can I proceed with your order? (yes/no): ")
    if call.lower() == "yes":
        print(f"Thank you for confirming your order. Enjoy your {menu_name}!\n")
        print(f"Total Bill: ₹{total}")
        print("🎉 Your meal is being prepared. Please wait... 🍽️")

        
        

    else:
        print("Order was not confirmed.!",name,"Can you please  tell me why are you canceled your order")
        print("""
          1-[Ordered wrong item]
          2-[Changed your mood]
          3-[Cleaning issue]
          4-[Order was too costly]
          5-[You dont like our service]
          6-[your reason is not listed]
          
              """)
        choice=input("please selected reason for cancelation of order >>")
        if choice == "1":
            print("No worries! Please take your time and reorder when ready.")
        elif choice == "2":
            print("Totally understandable. Come back whenever you're hungry!")
        elif choice == "3":
            print("We're sorry for the inconvenience. We'll work on maintaining better hygiene.")
        elif choice == "4":
            print("We understand! Maybe try our daily deals or economy combos.")
        elif choice == "5":
             print("We apologize. Please let us know how we can serve you better.")
        elif choice == "6":
           custom_reason = input("Please share your reason: ")
        print("Thank you for your feedback. We value every opinion.")

    # ✅ Exit the program after confirming or declining
    exit()


def breakfast():
    menu = {
        "1": ("Idli Sambhar", 200),
        "2": ("Masala Dosa", 220),
        "3": ("Paneer Dosa", 250),
        "4": ("Plain Dosa", 180),
        "5": ("Onion Dosa", 190)
    }
    return take_order("breakfast", menu)


def lunch():
    menu = {
        "1": ("Veg Thali", 300),
        "2": ("Paneer Butter Masala with Naan", 250),
        "3": ("Dal Makhani with Rice", 220),
        "4": ("Rajma Chawal", 180),
        "5": ("Mix Veg with Roti", 200)
    }
    return take_order("lunch", menu)


def dinner():
    menu = {
        "1": ("Veg Biryani", 250),
        "2": ("Shahi Paneer with Roti", 240),
        "3": ("Malai Kofta with Naan", 260),
        "4": ("Chole Bhature", 210),
        "5": ("Tandoori Roti & Sabzi", 230)
    }
    return take_order("dinner", menu)


# Main Program
print("👋 Welcome to our Restaurant!")
name = input("May I know your name please? >> ")
if name == "no":
    print("OK SIR PLEASE VISIT NEXT TIME")
    exit()
else:
   print(f"\nWelcome, {name}! We hope you have a great dining experience.")

total_bill = 0

while True:
    print("\nWhat would you like to have?")
    print("1 = Breakfast\n2 = Lunch\n3 = Dinner\n4 = Exit")

    choice = input("Please enter your choice (1/2/3/4): ")

    if choice == "1":
        total_bill += breakfast()
    elif choice == "2":
        total_bill += lunch()
    elif choice == "3":
        total_bill += dinner()
    elif choice == "4":
        print("Thanks for visiting",name,)
        exit()
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
        break