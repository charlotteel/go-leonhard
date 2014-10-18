def palindrome(x):
	if str(x) == str(x)[::-1]:
		return True
	else:
		return False

palinlist = []

for x in range(100,1000):
	for y in range(100,1000):
		result = x * y
		if palindrome(result) == 1:
			palinlist.append(result)

palinlist.sort()

print palinlist[len(palinlist)-1]
		
