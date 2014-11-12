def sumsquares(x):
    total = 0
    for i in range(1,x+1):
        total = total + (i**2)
    return total

a = sumsquares(100)

def squaresum(x):
    total = 0
    for i in range(1,x+1):
        total = total + i
    return total**2

b = squaresum(100)

print (b-a)
