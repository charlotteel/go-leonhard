# Find millionth lexicographic permutation of digits 0-9

import math
nums = [10,9,8,7,6,5,4,3,2,1]
facs = []
for i in range(0,len(nums)):
    facs.append(math.factorial(nums[i]))

# facs result [3628800, 362880, 40320, 5040, 720, 120, 24, 6, 2, 1]
# 3628800 total permutations of 10 digits, 362880 of 9 digits etc

permut = 1000000
digpos = []
def findmults(facpos):
    for i in range(1,10):
        tot = permut - (i*facs[facpos])
        if tot <= 0:
            digpos.append(i-1)
            return permut - ((i-1)*facs[facpos])
            break

for i in range(1,10):
    permut = findmults(i)

digpos.append(0)
digits = [0,1,2,3,4,5,6,7,8,9]

def makenum():
    numinorder = ""
    for i in range(0,10):
        pos = digpos[i]
        val = digits[pos]
        numinorder = numinorder + str(val)
        digits.remove(val)
    return numinorder

print makenum()
    
