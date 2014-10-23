def maketriangs(x):
    # make an array of x triangle numbers
    triangs = [1]
    for i in range(2,x+1):
        nxt = triangs[len(triangs)-1] + i
        triangs.append(nxt)
    return triangs

tris = maketriangs(20000000)
# arbitrary giant bunch of triangle numbers

def findprimes(x):
    # find all primes up to x
    candidates = [True] * (x+1)
    candidates[0] = False
    candidates[1] = False
    for i in range(2,int(x**0.5)+1):
        if candidates[i] == True:
            for j in range (i**2,x+1,i):
                candidates[j] = False
    return candidates

def listem(x):
    # list all primes up to x
    primelist = findprimes(x)
    primes = []
    for i in range(0,len(primelist)):
        if primelist[i] == True:
            primes.append(i)
    return primes

primes = listem(10000)
# gives 1229 primes

# a number that breaks down entirely to a quantity of unique prime factors has
# the highest number of divisors for that quantity of factors.

# 4 unique prime factors gives 16 divisors
# 5 gives 32, 6 gives 64, 7 gives 128, 8 gives 256 divisors

def minprod(x):
    # multiplies x unique prime factors to find 2^x divisors
    minprod = 1
    for i in range(0,x):
        minprod = minprod * primes[i]
    return minprod

startpt = minprod(8)
# gives smallest product of 8 primes (9699690)
# which is smallest number to have 256 divisors

abovemin = filter(lambda y: y >= startpt, tris)
# print len(abovemin)
# len shows 19995597 triangle numbers left

def numdivs(x):
    # find all divisors
    divs = []
    for i in range(1,(int(x**0.5))+1):
        if x % i == 0:
            divs.append(i)
    otherdivs = []
    if (x**0.5) % 1 == 0:
        for i in range(0,len(divs)-1):
            other = x / divs[i]
            otherdivs.append(other)
    else:
        for i in range(0,len(divs)):
            other = x / divs[i]
            otherdivs.append(other)
    all = divs + otherdivs
    all.sort()
    howmany = len(all)
    return howmany

# edited numdivs(19995597) to print "all" and temporarily list divisors
# to decide on possible factors to use as steps in next function

def divoftris(x):
    # narrows it down using steps of 9
    for i in range(0,len(x),9):
        if numdivs(x[i]) > 500:
            return i
            break

newmax = divoftris(abovemin)

def seconddiv(x,y):
    for i in range(0,y+1):
        if numdivs(x[i]) > 500:
            return x[i]
            break

print seconddiv(abovemin,newmax)
