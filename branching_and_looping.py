from functions import *

def integers_from_start_to_end_using_range(start, end, step):
    """return a list"""
    numbers=[]
    for i in range(start,end,step):
    	numbers.append(i)
    return numbers


def integers_from_start_to_end_using_while(start, end, step):
    """return a list"""
    num=[]
    if step>0:
    	if start<end:
    		while start<end:
    			num.append(start)
    			start+=step
    		return num
    	else:
    		print('not valid input')
    elif step<0:
    	if start>end:
    		while start>end:
    			num.append(start)
    			start+=step
    		return num
    	else:
    		print('not valid input')
    else:
    	print('not valid')




def two_digit_primes():
    """
    Return a list of all two-digit-primes
    """
    num=[];
    i=0;
    for x in range(11,100,2):
        i=0
        for y in range(3,10):
            if x%y==0:
                i+=1
                break
        if i==0:
            num.append(x)
        '''
        #logic 2
        if is_prime(x):
            num.append(x)
        '''


        '''# logic 3
    	i=0;
    	for y in range(2,int(x/2)):
    		if x%y==0:
    			i+=1
    			break
    	if i==0:
    		num.append(x)
        '''
    return num
    			
    			
