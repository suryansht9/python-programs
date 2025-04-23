#argument in python
'''def greet(name):  # 'name' is a parameter
    print("Hello", name)

greet("suryansh") ''' # "suryansh" is the argument
'''def put(a,b):
    if(a%2==0):
        print('a is divisble by 2:')
    elif(b%2==0):
        print('b is divisble by 2:')
    else:
        print('Your both value is not divisble by 2')

print('hello user here is your solution of given value it is divisble by 2 or not')
put(5,7)'''
#programe for argument
'''def get_snack(money):
    if money >= 2:
        print("Here’s your chocolate 🍫")
    else:
        print("Not enough money 😢")

get_snack(4)'''
def is_palindrome():
    user_input = input("Enter a number or word: ")
    if user_input == user_input[::-1]:
        print("user_input is a palindrome ✅")
    else:
        print("{user_input} is NOT a palindrome ❌")

# Call the function
is_palindrome()
