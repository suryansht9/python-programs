def show_menu():
    print("\nSelect an item to buy:")
    print("1. Clothes - $50")
    print("2. Electronics - $200")
    print("3. Groceries - $30")
    print("4. Exit and Checkout")

def main():
    total = 0.0
    print("🛍️ Welcome to the Shopping Mall 🛍️")

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            qty = int(input("Enter quantity: "))
            total += qty * 50
        elif choice == '2':
            qty = int(input("Enter quantity: "))
            total += qty * 200
        elif choice == '3':
            qty = int(input("Enter quantity: "))
            total += qty * 30
        elif choice == '4':
            print(f"\n🧾 Total bill: ${total:.2f}")
            print("Thank you for visiting the Shopping Mall!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
