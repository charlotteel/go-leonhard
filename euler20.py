import math
facto = math.factorial(100)
facto = str(facto)

def digitsum(x):
    total = 0
    for i in range(0,len(x)):
        total = total + int(x[i])
    return total

print digitsum(facto)
        
