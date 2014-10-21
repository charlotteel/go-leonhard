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

listy = findprimes(2000000)

def additup(primelist):
    primetot = 0
    for i in range(0,len(primelist)):
        if primelist[i] == True:
            primetot = primetot + i
    return primetot

print additup(listy)
        
