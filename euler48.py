mylist = list(range(1,1001))
mylist = list(map((lambda x: x**x), mylist))
print reduce((lambda x,y: x+y),mylist)

