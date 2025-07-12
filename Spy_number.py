num = int(input("Enter a number: "))
sum_digits = 0
product_digits = 1

for digit in str(num):
    sum_digits += int(digit)
    product_digits *= int(digit)

if sum_digits == product_digits:
    print("Spy Number")
else:
    print("Not a Spy Number")
