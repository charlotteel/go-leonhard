namelist = open("names.txt", "r")
allnames = namelist.read()
allnames = allnames.translate(None, '"')
allnames = allnames.split(',')
allnames.sort()
namevals = []

for i in range(0,len(allnames)):
    name = str(allnames[i])
    nametot = 0
    for j in range(0,len(name)):
        val = ord(name[j]) - 64
        nametot += val
    namevals.append(nametot)

scores = []    
for a in range(0,len(allnames)):
    mult = namevals[a] * (a+1)
    scores.append(mult)

additup = 0
for z in range(0,len(scores)):
    additup += scores[z]

print additup
    
namelist.close()
