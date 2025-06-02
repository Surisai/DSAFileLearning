
def one(mylist, key):
	total = 0 # 1 
	for i in range(len(mylist)): #  n + n-1
		for j in range(i+1,len(mylist)):   # n-1 + 1(n-1) +2(n-2) + 1
			if i != j:  # n-1 
				if mylist[i] + mylist[j] == key: # 
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