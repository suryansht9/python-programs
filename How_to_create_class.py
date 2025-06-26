class Record:
    def __init__(self):
        self.name = "Suryansh"
        self.age = 21
        self.address = "Pratapgarh"
        self.mobile = 72376264

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"Mobile No: {self.mobile}")

# Create an object
person = Record()

# Call the method
person.display_info()
