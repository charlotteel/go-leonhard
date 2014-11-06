def sumdiags(x):
    sum = 1
    val = 1
    for i in range(2,x,2):
        for j in range(1,5):
            val += i
            sum += val
    return sum

print sumdiags(1001)
