def is_prime(x):
        # check if x is prime
	if x < 2:
		return False
	elif x == 2:
		return True
	else:
		for i in range(2,int(x)):
			rem = x % i
			if rem == 0:
				return False
		else:
			return True

def inputfac(num):
        # return list of prime factors of num
        primelist = []
        nonlist = []
        faclist = range(2,num+1)
        for i in range(0,len(faclist)):
                if is_prime(faclist[i]) == 1:
                        primelist.append(faclist[i])
                else:
                        nonlist.append(faclist[i])
        return primelist

def findfacs(maxi):
        # find prime factors that occur more than once in producing solution
        global primelist
        primelist = inputfac(maxi)
        rt = int(maxi**0.5)
        prlst = filter(lambda x: x <= rt, primelist)
        return prlst

prlst = findfacs(20)

def findpower(x,maxi):
        # find what power those primes must be raised to
        n = 1
        while x ** n < maxi:
                n += 1
        return n-1

def multfacs(prlst,maxi):
        #  add the extra occurrences of those primes
        multlist = []
        for i in range(0,len(prlst)):
                val = prlst[i]
                j = findpower(val,maxi)-1
                templist = [val] * j
                multlist = multlist + templist
        return multlist

toadd = multfacs(prlst,20)
allfactors = toadd + primelist
allfactors.sort()
# acquired a complete list of factors needed to find smallest product

def mult_it_out(allfactors):
        total = 1
        for i in range(0,len(allfactors)):
                total = total * allfactors[i]
        return total

anstot = mult_it_out(allfactors)
print anstot                       

