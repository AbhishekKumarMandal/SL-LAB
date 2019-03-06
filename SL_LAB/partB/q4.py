from operator import itemgetter
from functools import reduce
def fun():
	f=open('letter.txt')
	d={}
	for i in f:
		l=i.split()
		for j in l:
			if j in d:
				d[j]+=1
			else:
				d[j]=1
	for key,value in d.items():
		print(key+" "+str(value))
	print
	l=sorted(d.items(),key=itemgetter(1),reverse=True)
	m=[]
	for i in range(0,10):
		m.append(l[i][1])
		print(l[i])
	print(m)
	
	# using reduce function
	avg=reduce(lambda a,b:a+b,m)/len(m)
	print('avg',avg)
	
	#using list comprehendion to find square of odd numbers
	z=[x**2 for x in range(1,11) if(x%2)!=0]
	print("list of square of odd nos form 1 t0 10:",z)
	
	#print(d.items())
fun()

# d.items() is a LIST of TUPLES for the given dictionary
# eg: [('and', 2), ('help', 1), ('is', 1)]
