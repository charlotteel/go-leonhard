def countlet():
    start = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    # 0 to 19
    rest = [0] * 981
    allnum = start + rest
    for i in range(0,10):
        allnum[i+20] = 6 + allnum[i]
    for i in range(0,10):
        allnum[i+30] = 6 + allnum[i]
    for i in range(0,10):
        allnum[i+40] = 5 + allnum[i]
    for i in range(0,10):
        allnum[i+50] = 5 + allnum[i]
    for i in range(0,10):
        allnum[i+60] = 5 + allnum[i]
    for i in range(0,10):
        allnum[i+70] = 7 + allnum[i]
    for i in range(0,10):
        allnum[i+80] = 6 + allnum[i]
    for i in range(0,10):
        allnum[i+90] = 6 + allnum[i]
    for i in range(1,10):
        allnum[i*100] = allnum[i] + 7
    for i in range(1,100):
        allnum[i+100] = allnum[100] + 3 + allnum[i]   
    for i in range(1,100):
        allnum[i+200] = allnum[200] + 3 + allnum[i] 
    for i in range(1,100):
        allnum[i+300] = allnum[300] + 3 + allnum[i]
    for i in range(1,100):
        allnum[i+400] = allnum[400] + 3 + allnum[i]
    for i in range(1,100):
        allnum[i+500] = allnum[500] + 3 + allnum[i]
    for i in range(1,100):
        allnum[i+600] = allnum[600] + 3 + allnum[i]
    for i in range(1,100):
        allnum[i+700] = allnum[700] + 3 + allnum[i]
    for i in range(1,100):
        allnum[i+800] = allnum[800] + 3 + allnum[i]
    for i in range(1,100):
        allnum[i+900] = allnum[900] + 3 + allnum[i]
    allnum[1000] = 11
    totalnum = 0
    for i in range(1,1001):
        totalnum = totalnum + allnum[i]
    return totalnum

print countlet()
