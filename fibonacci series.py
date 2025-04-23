def fibonacci_series():
    n = int(input("Enter how many Fibonacci numbers you want: "))

    a, b = 0, 1  # First two numbers
    print("Fibonacci sequence:")

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Call the function
fibonacci_series()
