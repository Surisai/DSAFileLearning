

num = 6
while True:
   if num % 5 == 0:
      print("First divisible by  :", num)
      break
   num +=1

while num <= 20:
   if num %5 ==0: 
    print ("Count : ", num)
   num +=1

   var = 0  # Assigning 0 to var
print(var == 0)

var = 1  # Assigning 1 to var
print(var == 0)

var = 0  # Assigning 0 to var
print(var != 0)
 
var = 1  # Assigning 1 to var
print(var != 0)

n = int(input())
print(n >= 100) # printTRU or False


# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

largest_number = number1
if number2 > largest_number:largest_number = number2
if number3 > largest_number: largest_number = number3
# Print the result
print("The largest number is:", largest_number)

# Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.

largest_number = max(number1, number2, number3) # wih min()

# Print the result.
print("The largest number is:", largest_number)

