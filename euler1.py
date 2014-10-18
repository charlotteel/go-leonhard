def firsteuler(argu):
	total = 0
	for i in range(0,len(argu)):
		if i % 3 == 0:
			total = total + i
		elif i % 5 == 0:
			total = total + i
	return total

list1 = range(0,1000)
print firsteuler(list1)