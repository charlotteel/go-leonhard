def sumdivs(x):
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
    sumofdiv = 0
    for i in range(0,len(all)-1):
        sumofdiv = sumofdiv + all[i]
    return sumofdiv

def findamic(x):
    amiclist = []
    for i in range(1,x):
        x = sumdivs(i)
        if sumdivs(x) == i and x != i:
            amiclist.append(i)
            amiclist.append(x)
    amiclist = list(set(amiclist))
    amiclist.sort()
    return amiclist

amiclist = findamic(10000)

def additup(listy):
    total = 0
    for i in range(0,len(listy)):
        total = total + listy[i]
    return total

print additup(amiclist)
        
        
        
