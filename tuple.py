# Creating a tuple
coordinates = (10, 20)

# Accessing
print(coordinates[1])  # 20

# Looping
for point in coordinates:
    print(point)

# Tuples are often used for fixed data
my_tuple = (10, 20, 30, 20, 40)

print(my_tuple.count(20))  # 2
print(my_tuple.index(30))  # 2

print(len(my_tuple))       # 5
print(sum(my_tuple))       # 120
print(min(my_tuple))       # 10
print(max(my_tuple))       # 40

converted = tuple([1, 2, 3])  # (1, 2, 3)
