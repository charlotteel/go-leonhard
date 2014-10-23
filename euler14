def collatz(x):
    col = [x]
    z = x
    while z != 1:
        if z % 2 == 0:
            z = z/2
            col.append(z)
        else:
            z = 3*z + 1
            col.append(z)
    return len(col)

def checknums(x):
    hilen = 1
    histart = 1
    for i in range(1,x):
        if collatz(i) > hilen:
            hilen = collatz(i)
            histart = i
    print hilen
    return histart

print checknums(1000000)
