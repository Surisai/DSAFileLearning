n = input("Enter the name of plant you like the most :  ")
if n == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif n == "spathiphyllum": print("No, I want a big Spathiphyllum!")

else: print("Spathiphyllum! Not pelargonium!")


# linear calculation

def linear_search(my_list, key):
    for i in range(0, len(my_list)):     # n + 2
        if my_list[i] == key:            # n
            return i                     # 0

    return -1                            # 1

# factorial function
print(linear_search(1,2,3,4,4,5), 4)
def fectorial(n):
    r = 1
    for i in range(2, n+1):
        r = r * i
    return r
    
print(fectorial(9,3,4,55),4)
