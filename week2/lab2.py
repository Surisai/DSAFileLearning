
def one(mylist, key):
	total = 0 #
	for i in range(len(mylist)): #  
		for j in range(i+1,len(mylist)): #3
			if i != j:  #
				if mylist[i] + mylist[j] == key: #2
					total += 1 # 
	return total # 

def two(mylist, key):
	total = 0 # 1 
	mylist.sort() # logn
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