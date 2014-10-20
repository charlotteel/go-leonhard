def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2,x):
            rem = x % i
            if rem == 0:
                return False
        else:
            return True
		    
def findprimes(w,x):
    primes = []
    for i in range(w,x+1):
        if is_prime(i) == 1:
            primes.append(i)
    return primes

def loopprimes(x):
    prlst = findprimes(1,x)
    newend = x
    while len(prlst) < 10001:
        newend += 200
        primes = findprimes(newend-199,newend)
        prlst = prlst + primes
    return prlst

ans = loopprimes(100000)
print ans[10000]
        
