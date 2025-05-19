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

