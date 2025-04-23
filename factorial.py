def factorial():
    import math  # Imported inside
    num = int(input("Enter a number to find its factorial: "))
    result = math.factorial(num)
    print(f"The factorial of {num} is {result}")


factorial()