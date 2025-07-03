'''
Big O notation (O) represents an upper bound on the growth rate of 
an algorithm's running time or space usage.

Big O tells us the worst-case scenario ó how the performance of an algorithm grows 
as the input size increases.

In other words, it gives us a guarantee that the algorithm will not be slower 
than this rate for large inputs.

In loop 
i=i+k or i=i-k >>>> O(n)
i=i*k or i=i/k  >>>>>> O(logn)
'''
# Example 0
s = 0  #1
i = 1  #1
while i < n: # n   
    s = s + i   #2(n-1) 
    i=i+1       #2(n-1) 

# T(n)= 1+1+n+2(n-1)+2(n-1)= 5n + 2-1-2-2=5n-2
# T(n) is O(n)

# Example 1
s = 0  #1
i = 1  #1
while i < n: # log(n)
    s = s + i  #2 log(n)
    i = i * 2  #2 log(n)

T(n)= ...= 2+ 5log(n)
T(n) is O(logn)
#----------------------------------------
# Example 2
s = 0  #1
i = n  #1
while i > 1: #log(n)
    s = s + i # 2logn
    i = i // 2 # 2logn
    
T(n) = ....= 2+5log(n) 
T(n) is O(log n)
#----------------------------------------
# Example 3          0 1 2 3 4 ..n-1
s = 0   # 1
for i in range(n): # n + 1
    for j in range(n):# n(n+1)
        s = s + i + j  # 3*n*n

T(n)= 1+n +1 +(n +1)n +3nn= 4n^2 + 2n +2
T(n) is O(n^2)
#----------------------------------------
# Example 4      i 0 2 4 6 8 10....
s = 0 #1
for i in range(0,n,2):  #1 +n/2
    for j in range(n): # (1+n)n/2
        s = s + i + j  # 3*n*n/2
T(n)=......
O(n^2)

#----------------------------------------
# Example 5
s = 0  #1
for i in range(0,n,-1): # 1+n
    for j in range(n): #(1+n)n
        s = s + i + j  # 3*n*n
# T(n)=1+ 1+n +(1+n)n+3*n* n=3n^2 +n^2 + n+3=..........
# T(n) is O(n^2)
# #-------------------------------------
# Example 6:
def linear_search(arr, target):
    for i in range(len(arr)): #1 + 1 + n
        if arr[i] == target:  #n
            return i          #0 
    return -1                 #1 , if it is fualt 
# T(n) = 3+ 2n, T(n) is O(n)
#-------------------------------------
# Example 8
s = 0 # 1
for i in range(n): # n +1 
    for j in range(n): # n(n+1)
        k = 1 # n^2<-- for i and j so n*n
        while k < n: # n^2logn
            s = s + i + j + k # 4(n^2logn)
            k = k * 2 # 2(n^2logn)
#T(n) = 2 + 2n + 2n^2 +6n^2logn 



# Example 9 (bubble sort-like)
def function3(lst):
    for i in range(0, len(lst) - 1): # 3+n-1 
        for j in range(0, len(lst) - 1 - i):#  n(n-1)/2 + n-1
            if lst[j] > lst[j + 1]:  # n(n-1)/2 + (n-1)
                tmp = lst[j] # n(n-1)/2 + (n-1)
                lst[j] = lst[j + 1] # n(n-1)/2 
                lst[j + 1] = tmp  #(n-1)/2 
    #T(n) = n + (n^2 -n) /2 + n-1 + 4((n^2 - n) /2)
        


