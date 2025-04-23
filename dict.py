# Creating a dictionary
'''person = {"name": "Alice", "age": 30, "city": "New York"}
print(person)'''

# Accessing
'''print(person["name"])'''  # Alice

# Modifying
'''person["age"] = 31
print(person)'''

# Adding new key-value
'''person["email"] = "alice@example.com"
print(person)'''

# Looping
'''for key, value in person.items():
    print(key, ":", value)
'''
#a small programe by me
'''t={"name":"suryansh","age":20,"Address":"prayagraj","college":"University of Alllahabad"}
print(t["Address"])
for A in t:
    print(t)
for key,value in t.items():
    print(key,":",value)'''

my_dict = {"name": "Alice", "age": 25, "city": "New York"}

print(my_dict["name"])          # Alice
print(my_dict.get("age"))       # 25
print(my_dict.get("email", "N/A"))  # N/A

my_dict["email"] = "alice@example.com"  # Add new key
my_dict.update({"age": 26})      # Update age

my_dict.pop("city")              # Removes 'city'
my_dict.setdefault("country", "USA")  # Adds if not exists

print(my_dict.keys())            # dict_keys(['name', 'age', 'email', 'country'])
print(my_dict.values())          # dict_values([...])
print(my_dict.items())           # dict_items([...])

copy_dict = my_dict.copy()       # Shallow copy
my_dict.clear()                  # Empty dict → {}
