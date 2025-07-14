def main():
    balance = 0.0
    print("🏦 Welcome to Simple Bank System 🏦")

    while True:
        print("\nSelect an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: $"))
            if amount > 0:
                balance += amount
                print("✅ Deposited successfully.")
            else:
                print("❌ Invalid amount.")

        elif choice == '2':
            amount = float(input("Enter amount to withdraw: $"))
            if 0 < amount <= balance:
                balance -= amount
                print("✅ Withdrawn successfully.")
            else:
                print("❌ Insufficient balance or invalid amount.")

        elif choice == '3':
            print(f"💰 Current Balance: ${balance:.2f}")

        elif choice == '4':
            print("👋 Thank you for visiting the bank!")
            break

        else:
            print("❗ Invalid choice! Try again.")

if __name__ == "__main__":
    main()
