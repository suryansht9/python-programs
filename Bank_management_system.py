

def loan():
    print("Hello sir/Mam may i help you")
    print("Sir/Mam you want loan from our bank")
    b=input("yes or no =")
    if b=="yes":
        print("Glad to have you here sir/mam please tell me Amount of your loan")  
        amount=int(input("Enter your amount here ="))
        if amount >= 50000:
            print("Sir\Mam you have to pay 1.5% interest in this amount")
            choice=input("can i proceed your loan file yes or no =")
            if choice == "yes":
                print("Ok sir i will transfer your file for final approval Congrats your loan has been approved")
            elif choice =="no":
                print("No problem sir/mam thankyou for visiting")
            else:
                print("I think you are confused sir/mam please choose right choice")
def account():
    print("Glad to have you here Sir/Mam. Please provide the following information so I can create your account.")

    name = input("Enter your Name: ")
    father_name = input("Enter your Father's Name: ")
    mother_name = input("Enter your Mother's Name: ")
    
    try:
        age = int(input("Enter your Age: "))
    except ValueError:
        print("Invalid input for age. Please enter a number.")
        return

    qualification = input("Enter your Qualification: ")
    account_type = input("Account Type (Saving/Current): ").lower()

    if account_type not in ["saving", "current"]:
        print("Invalid account type. Please choose either 'Saving' or 'Current'.")
        return

    print("\nThanks for providing all the information.")
    proceed = input("Sir/Mam, can I proceed with your file? (yes or no): ").lower()

    if proceed == "yes":
        print("Congrats Sir/Mam, your account has been successfully created.")
    elif proceed == "no":
        print("No problem Sir/Mam. Thank you for visiting.")
    else:
        print("Invalid choice. Please respond with 'yes' or 'no'.")

 
def fd():
    print("Glad to have you here Sir/Mam. Please provide the details below so I can proceed with your FD.")

    name = input("Enter your Name: ")
    father_name = input("Enter your Father's Name: ")
    mother_name = input("Enter your Mother's Name: ")
    
    try:
        age = int(input("Enter your Age: "))
        qualification = input("Qualification: ")
        amount = int(input("Enter the amount for Fixed Deposit: "))
        years = int(input("Enter the time period (in years): "))
    except ValueError:
        print("Please enter valid numeric values for age, amount, and years.")
        return

    # Determine interest rate based on amount
    if amount < 100000:
        rate = 4
        print("Your amount is below ₹1 Lakh. You will get 4% interest.")
    elif amount < 500000:
        rate = 12
        print("Your amount is between ₹1 Lakh and ₹5 Lakhs. You will get 12% interest.")
    else:
        rate = 18
        print("Your amount is above ₹5 Lakhs. You will get 18% interest.")

    # Calculate maturity amount (Simple Interest)
    interest = (amount * rate * years) / 100
    maturity_amount = amount + interest

    print(f"\nSummary:")
    print(f"Name: {name}")
    print(f"Deposit Amount: ₹{amount}")
    print(f"Time Period: {years} years")
    print(f"Interest Rate: {rate}%")
    print(f"Total Interest: ₹{interest}")
    print(f"Total Maturity Amount: ₹{maturity_amount}")

    confirmation = input("\nAre you satisfied with our service? Shall I proceed to fix your deposit? (yes/no): ").lower()

    if confirmation == "yes":
        print("Congrats Sir/Mam, your FD file has been sent to our department.")
    elif confirmation == "no":
        print("No problem Sir/Mam. Thank you for visiting.")
    else:
        print("Please enter a correct confirmation (yes or no).")


def withdrawal():
    print("Glad to have you here Sir/Mam. Please provide the following information so I can proceed with your withdrawal.")

    name = input("Enter your Name: ")
    account_number = input("Enter your Account Number: ")
    
    try:
        amount = int(input("Enter Withdrawal Amount: "))
        if amount <= 0:
            print("Invalid amount. Please enter a positive value.")
            return
    except ValueError:
        print("Invalid input. Please enter a numeric value for the amount.")
        return

    account_type = input("Account Type (Saving/Current): ").lower()
    if account_type not in ["saving", "current"]:
        print("Invalid account type. Please choose either 'Saving' or 'Current'.")
        return

    confirm = input(f"Do you want to proceed with withdrawing ₹{amount}? (yes/no): ").lower()
    if confirm == "yes":
        print(f"₹{amount} has been **debited** from Account Number {account_number}.")
        print("Thank you for using our service.")
    elif confirm == "no":
        print("Transaction cancelled. Thank you for visiting.")
    else:
        print("Invalid response. Please answer with 'yes' or 'no'.")

def deposit():
    print("Glad to have you here Sir/Mam. Please provide the following information so I can deposit money for you.")

    name = input("Enter your Name: ")
    account_number = input("Enter your Account Number: ")
    
    try:
        amount = int(input("Enter Deposit Amount in ₹: "))
        if amount <= 0:
            print("Invalid amount. Please enter a positive value.")
            return
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    account_type = input("Account Type (Saving/Current): ").lower()
    if account_type not in ["saving", "current"]:
        print("Invalid account type. Please choose either 'Saving' or 'Current'.")
        return

    print(f"₹{amount} has been **credited** to your Account Number {account_number}.")
    print("Thank you for banking with us, Sir/Mam!")

while True:
    print("\n🔷 Welcome to Our Bank, Sir/Mam 🔷")
    print("Please enter your choice:")
    print("1 = Apply for Loan")
    print("2 = Create an Account")
    print("3 = Enquiry for Fixed Deposit (FD)")
    print("4 = Cash Withdrawal")
    print("5 = Cash Deposit")
    print("6 = Exit")

    try:
        choice = int(input("Enter your choice (1/2/3/4/5/6): "))
        if choice == 1:
            loan()
        elif choice == 2:
            account()
        elif choice == 3:
            fd()
        elif choice == 4:
            withdrawal()
        elif choice == 5:
            deposit()
        elif choice == 6:
            print("🔒 Thank you for visiting our bank. Have a great day!")
            break
        else:
            print("❌ Invalid choice. Please select a number between 1 and 6.")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
