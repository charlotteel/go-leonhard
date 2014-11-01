# finding numbers that can be written as sum of 5th power of digits

highest = 0
for i in range(1,10):
    val = i*(9**5)
    if len(str(val)) >= i:
        highest = val

# highest = 354294 so only need to search up to this number
# lowest? problem specifies single-digit numbers don't count as summing digits

powsums = []
for i in range(10,highest+1):
    sumit = 0
    for j in str(i):
        sumit += int(j)**5
    if sumit == i:
        powsums.append(i)

finaltot = 0
for i in range(0,len(powsums)):
    finaltot += powsums[i]

print finaltot
