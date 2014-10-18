def is_prime(x):
    
	if x < 2:
        
		return False
    
	elif x == 2:
        
		return True
    
	else:
        
		for i in range(2,x):
            
			rem = x % i
            
			if rem == 0:
                
				return False
       
		else:
            
			return True

def factorfind(num):
	factors = []
	for i in range(1,num):
		if num % i == 0:
			if is_prime(i) == 1:
				factors.append(i)
	return factors

primefactors = factorfind(13195)
print primefactors[(len(primefactors)-1)]