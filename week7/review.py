#Recursive Part

def function1(value, number):
	if (number == 0): #1
		return 1
	elif (number == 1):#1
		return value
	else:
		return value * function1(value, number-1) # 2 + T(n-1)
	

    #T(n) = 1
	
#T(n) = 4n-3



def recursive_function2(mystring,a, b):
	if(a >= b ): #1
		return True
	else:
		if(mystring[a] != mystring[b]): #1
			return False
		else:
			return recursive_function2(mystring,a+1,b-1)#2 + T(n-2)
#T(n) = 4 +t(n-2)
#      = 4(4+T(n-2)) = 4+$+$+ T(n-6) = 
# T(n) = 4*n/2+2
def function2(mystring):
	return recursive_function2(mystring, 0,len(mystring)-1) #2 + 4(n/2) +2 == 2 +O(n)

# 


def function3(value, number):
	if (number == 0):#1
		return 1
	elif (number == 1):#1
		return value
	else:
		half = number // 2 #2(logn)
		result = function3(value, half) #  1 + T(n/2)
		#this belove will no executed bc: result = function3(value, half) already executed so the program will stop 
		# and the control will return back to first condition
		if (number % 2 == 0): #2
			return result * result 
		else: # 
			return value * result * result # 2 


#T(1) = 3 
#T(n) = 9 + T(n/2)
#T(n/2) = 9 + T(n/4)


T(n) = 9 + T(n/2)
     = 9