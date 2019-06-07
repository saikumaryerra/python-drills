def is_prime(n):
	if n==1:
		return False
	i=0
	for x in range(2,int(n/2+1)):
		if n%x==0:
			i+=1
			break
	if i==0:
		return True
	else:
		return False



def n_digit_primes(digit = 2):
    """
    Return a list of `n_digit` primes using the `is_prime` function.

    Set the default value of the `digit` argument to 2
    """
    num=[]
    x=1
    if digit==1:
    	num=[2]
    	x=0

    for x in range(int((10**(digit-1))+x),10**digit,2):
    	if is_prime(x):
            num.append(x)
    return num