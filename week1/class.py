class Student:
    #self - define belong to only this class 
    #to implement function ass salf

    def __init__(self, name, age): # 2 arguments
        self.name = name            # public attribute
        self.__age = age            # "__" double to define private attribute
# this function method

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.__age}")

    def get_age(self):             # getter for private attribute
        return self.__age

    def set_age(self, new_age):    # setter for private attribute
        if new_age > 0:
            self.__age = new_age

# Create student object 
student1 = Student("Bob", 21)
student1.display_info()

# Access public attribute
print("Access name:", student1.name)

# Try to access private attribute directly (will raise error if uncommented)
# print(student1.__age)

# Use getter/setter for private attribute
print("Age (via getter):", student1.get_age())
student1.set_age(22)
print("Updated Age (via getter):", student1.get_age())





