

# column  for () " : : :  "
def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

def greet_user(name):
    return f"Hello, {name}! Welcome to the course."
#example valueble with if you need varianle name you  with f + { }
def greet_user(name):
    return f"Hello, {name}! Welcome to the course."

# Test the functions
my_grades = [75, 80, 95]
average = calculate_average(my_grades)
print("Average grade:", average)

message = greet_user("Alice")
print(message)
