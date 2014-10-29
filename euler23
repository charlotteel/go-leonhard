def abundant(x):
    # check if x is abundant
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
    if sumofdiv > x:
        return True

def makelist(x):
    abunlist = []
    for i in range(1,x):
        if abundant(i) == True:
            abunlist.append(i)
    return abunlist

abunlist = makelist(28124)

def abunsum():
    notabunsum = [0]*28125
    for i in range(0,len(abunlist)):
        for j in range(0,len(abunlist)):
            val = abunlist[i] + abunlist[j]
            if val < 28125:
                notabunsum[val] = 1
    return notabunsum

notabunsum = abunsum()

def addup(somethings):
    total = 0
    for i in range(0,len(somethings)):
        if somethings[i] == 0:
            total = total + i
    return total

print addup(notabunsum)
