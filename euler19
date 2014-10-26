dayyear = [0]*365
dayyear[0] = 1
dayyear[31] = 1
dayyear[59] = 1
dayyear[90] = 1
dayyear[120] = 1
dayyear[151] = 1
dayyear[181] = 1
dayyear[212] = 1
dayyear[243] = 1
dayyear[273] = 1
dayyear[304] = 1
dayyear[334] = 1

leapyr = [0]*366
leapyr[0] = 1
leapyr[31] = 1
leapyr[60] = 1
leapyr[91] = 1
leapyr[121] = 1
leapyr[152] = 1
leapyr[182] = 1
leapyr[213] = 1
leapyr[244] = 1
leapyr[274] = 1
leapyr[305] = 1
leapyr[335] = 1

fourcycle = dayyear*3 + leapyr
century = fourcycle*25         

def findsun(list):
    totalsun = 0
    for i in range(5, len(list), 7):
        if list[i] == 1:
            totalsun = totalsun + 1
    return totalsun
        
print findsun(century)
