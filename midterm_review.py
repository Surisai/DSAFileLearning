# Example 1
s = 0 # 1
i = 1 # 1
while i < n: #  n
    s = s + i #  2(n-1)
    i = i + 1#  2(n-1) <----this incresement by +1 
# T(n) = 1+1 +5n
# T(n) = O(n)
 # Example 2
s = 0 # 1 
i =  # 1 
while i < n: # logn
    s = s + i #2logn
    i = i * 2 # 2(logn) <---- this part increment by *2 
# T(n) = 5 logn +2
# Example 3
s = 0 # 1 
i = n #  1
while i > 1:  # logn  
    s = s + i #  2log n 
    i = i // 2 # < ---  2(logn ) + 1
# T(n) = 
# 
# Example 4
s = 0 # 1 
for i in range(n): # n+1
    for j in range(n):  # n(n+1)
        s = s + i + j # 3 (n*n)
# T(n) = 1 + n +1 + n^2 + n + 3n^2 = 2 + 2n + 4n^2 ; T(n) is O(n^2)
# Example 5
s = 0 # 1
for i in range(0, n, 2): # n/2 +1 
    for j in range(n): # n(n/2 +1)/2 
        s = s + i + j # 3 (n/2  *n )
 # T(n) = 2 + n/2 + n^2 /2  + n/ 2+ 3n^2 /2    = 2 + n + 2n^ 2
# Example 6
s = 0 # 1 
for i in range(0, n, -1): # n+1
    for j in range(n):# n(n+1)
        s = s + i + j#  3(n * n )
# T(n) = 
# T
# Example 7 (linear search)
def linear_search(arr, target):
    for i in range(len(arr)): # n 
        if arr[i] == target: # 
            return i
    return -1

# Example 8
s = 0
for i in range(n):
    for j in range(n):
        k = 1
        while k < n:
            s = s + i + j + k
            k = k * 2

# Example 9 (bubble sort-like)
def function3(lst):
    for i in range(0, len(lst) - 1):
        for j in range(0, len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                tmp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = tmp



#example 9 
def function1(number):
	total = 0

	for i in range(number):
		x = i + 1
		total += x * x

	return total

#example 10
def function2(number):
	return (number * (number + 1) * (2 * number + 1)) // 6
#example 11
def function3(list):
	n = len(list)
	for i in range(n - 1):
		for j in range(n - 1 - i):
			if list[j] > list[j+1]:
				tmp = list[j]
				list[j] = list[j+1]
				list[j + 1] = tmp

#example 11
def function4(number):
	total = 1
	for i in range(1, number):
		total *= i + 1
	return total
#xmple 12

def one(mylist, key):
	total = 0
	for i in range(len(mylist)):
		for j in range(i+1,len(mylist)):
			if i != j:
				if mylist[i] + mylist[j] == key:
					total += 1
	return total

def two(mylist, key):
	total = 0
	mylist.sort()
	i = 0
	j = len(mylist)-1
	while (i < j):
		if(mylist[i] + mylist[j] < key):
			i+=1
		elif(mylist[i] + mylist[j] > key):
			j-=1
		else:
			total += 1
			i+=1
			j-=1
	return total

def three(mylist, key):
	items={}
	total = 0
	for number in mylist:
		items[number]=1
	for number in mylist:
		other = key-number
		if(other in items):
			total+=1
	return total//2




# example 12
def f1(number):
    rc = 1
    for i in range(0, 5):
        rc += 1
    return rc
# example 13
