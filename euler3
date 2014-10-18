def factorfind(num):
	factors = []
	for i in range(1,int(num**0.5)):
		if num % i == 0:
			factors.append(i)
	return factors

def is_prime(x):
	if x < 2:
		return False
	elif x == 2:
		return True
	else:
		for i in range(2,int(x**0.5)):
			rem = x % i
			if rem == 0:
				return False
		else:
			return True

firstfactors = factorfind(600851475143)
baselist = [600851475143] * len(firstfactors)
for i in range(0,len(firstfactors)):
                baselist[i] = baselist[i]/firstfactors[i]
allfactors = firstfactors + baselist
allfactors.sort()

primefactors = []
for i in range(1,len(allfactors)-1):
        if is_prime(allfactors[i]) == 1:
                primefactors.append(allfactors[i])

print primefactors[len(primefactors)-1]
