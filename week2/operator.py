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



#Example 4

s = 0 #1
for i in range(0,n,2): # increase by 2 so O 1 + n/2
    for j in range(n): # (1+n) n/2
        s = s + i + j # 3*n*n/2

#T(n) = 1 + 1+ n/2 + 1

#---------------------
#example 5

s =0#1
for i in range(0,n, -1): # count by reverse of number -1 . ( 1 + n )
    for j in range(n -1): # (1+n)n
        s = s +i +j # 3*n*n

    # T(n) = 
    # T(n) is O(n)

#---------------------
#example 6



#binary search  you have ti devide by 2 to find the number 
def binary_search(my_list, key):
    rc = -1 #1 
    low = 0 #1 
    high = len(my_list) - 1 #1 +2

    while rc == -1 and low <= high: # 
        mid = (low + high) // 2  # 3 *
        if key < my_list[mid]:  # 1
            high = mid - 1 # 2
        elif key > my_list[mid]: # 0 coz if condition execute 
            low = mid + 1 # 0
        else:       # 
            rc = mid # 

    return rc

def binary_search(my_list, key):
    rc = -1 #1 
    low = 0 #1 
    high = len(my_list) - 1 #1 +2
# == :1 , and :1, <=: 1, = 3 with while condition  : (1+log_n)
    while rc == -1 and low <= high: # 3 *(1 +log_n)
        mid = (low + high) // 2  # 3 * (1+log_n)
        if key < my_list[mid]:  # 1 +log_n
            high = mid - 1 # 0  this is no execute  then will consider other case
        elif key > my_list[mid]: # 1 +log_n
            low = mid + 1 # 2 * (1+log_n)
        else:       # 0
            rc = mid # 0

    return rc

# Example 8


s = 0 # 1
for i in range(n): # n+1
    for j in range(n): # n(n+1)
        k =1 # n * n
        while k < n : # n * n * log_n
            s = s + i +j + k # 4 *n*n* log(n)
            k= k * 2          #n*n*2log(n)
# T(n)=..............
#  T(n) is O(n^2log(n))