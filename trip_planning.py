print("Trip Budget Calculator by Suryansh")
name = input("Please enter your name: ")
f = input("Where do you want to travel? ")

a = int(input("Hey " + name + ", please enter your destination distance in kilometers: "))
b = int(input("Now please " + name + ", enter your expense in toll tax (in Rs): "))
c = int(input("Now " + name + ", please enter your expense in food (in Rs): "))
d = int(input("Now " + name + ", please enter the quantity of fuel needed (in liters): "))
e = int(input("Now " + name + ", please enter the price of fuel per liter (in Rs): "))

fuel_cost = d * e
total_expense = b + c + fuel_cost

print("\nAccording to your inputs, here's your total trip expense breakdown:\n")
print("Destination:", f, "- a very beautiful place!")
print(name + ", you want to explore " + f + ", which is " + str(a) + " kilometers away.")
print("Toll tax: Rs", b)
print("Food expense: Rs", c)
print("Fuel needed: ", d, "liters at Rs", e, "per liter.")
print("Total fuel cost: Rs", fuel_cost)
print("\nYour total trip expense is: Rs", total_expense)
