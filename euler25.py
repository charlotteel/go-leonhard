def findthou():
    fibon = [1,1]
    for i in range(2,10000):
        num = fibon[i-1] + fibon[i-2]
        fibon.append(num)
        if len(str(num)) == 1000:
            print i+1
            break

findthou()
