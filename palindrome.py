def is_palindrome():
    user_input = input("Enter a number or word: ")
    if user_input == user_input[::-1]:
        print(f"'{user_input}' is a palindrome ✅")
    else:
        print(f"'{user_input}' is NOT a palindrome ❌")

# Call the function
is_palindrome()
