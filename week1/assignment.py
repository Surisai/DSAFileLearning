class Employees:
    def __init__(self, id, name, position, salary):
        self.id = id
        self.name = name
        self.position = position
        self.__salary = salary

    def display_info(self):
        print(f"Employee ID : {self.id}")
        print(f"Employee Name : {self.name}")
        print(f"Position : {self.position}")
        print(f"Employee Salary : {self.__salary}\n")

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):  # <-- Renamed method
        if new_salary > self.__salary:
            self.__salary = new_salary
        else:
            print("You don't get any increase")


# Test the class
employee1 = Employees("0001", "Mhork", "Business Analyst", 9999999)
employee1.display_info()

print("Access position:", employee1.position)

print("Salary (with getter):", employee1.get_salary())

employee1.set_salary(777777)  # Try lower salary (no increase)
print("Updated salary (via getter):", employee1.get_salary())

print("This is reult of the year: \n")
employee1.set_salary(10000000)  # Try higher salary
print("Updated salary (via getter):", employee1.get_salary())
