def makelist(a,b):
    combos = []
    for i in range(a,b+1):
        for j in range(a,b+1):
            val = i**j
            combos.append(val)
            combos = list(set(combos))
    combos.sort()
    return len(combos)

print makelist(2,100)
            
