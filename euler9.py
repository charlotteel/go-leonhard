def findtriple():
    for a in range(1,1000):
        b = (500000 - (1000*a))/(1000 - a)
        c = 1000 - a - b
        if c**2 == a**2 + b**2 and 0 < b < 1000 and 0 < c < 1000:
            print a*b*c

findtriple()
