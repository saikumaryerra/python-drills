f = open('sai', 'w+')
for i in range(10):
	j=i+1
	f.write("{},{}\n".format(j,j**2))
f.close
    