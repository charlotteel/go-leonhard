def fibonacci(argu):
	startlist = argu
	lth = len(startlist)
	new = startlist[lth-2] + startlist[lth-1]
	while new <= 4000000:
		startlist.append(new)
		lth = len(startlist)
		new = startlist[lth-2] + startlist[lth-1]
	return startlist

list2 = [1,2]
list3 = fibonacci(list2)

def addevens(argu):
	total = 0
	for i in range(0,len(argu)):
		if argu[i] % 2 == 0:
			total = total + argu[i]
	return total

print addevens(list3)