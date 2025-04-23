# Creating a list
'''fruits = ["apple", "banana", "cherry"]
'''
# Accessing
'''print(fruits[0])  # apple
'''
# Modifying
'''fruits[1] = ("orange")
print(fruits)'''

# Adding
'''fruits.append("grape")
print(fruits)'''

# Looping
'''for a in fruits:
    print(a)'''

my_list = [10, 20, 30, 20, 50]

my_list.append(60)     # [10, 20, 30, 20, 50, 60]
my_list.extend([70, 80])   # [10, 20, 30, 20, 50, 60, 70, 80]
my_list.insert(2, 25)      # [10, 20, 25, 30, 20, 50, 60, 70, 80]
my_list.remove(20)         # removes first 20 → [10, 25, 30, 20, 50, 60, 70, 80]
my_list.pop()              # removes last → 80
my_list.pop(2)             # removes 3rd item → 30
my_list.clear()            # []

# Other operations
numbers = [5, 1, 8, 3]
print(numbers.index(8))    # 2
print(numbers.count(1))    # 1
numbers.sort()             # [1, 3, 5, 8]
numbers.reverse()          # [8, 5, 3, 1]
copy_list = numbers.copy() # [8, 5, 3, 1]

print(len(numbers))        # 4
print(sum(numbers))        # 17
print(min(numbers))        # 1
print(max(numbers))        # 8

