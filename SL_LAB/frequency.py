def fun():
	s=input("enter your string:")
	o=open("letter.txt",'w')
	o.write(s)
	o.close()
	f=open('letter.txt')
	d={}
	for i in f: # iterating row by row
		l=i.split()
		for j in l:
			if(j in d):
				d[j]+=1
			else:
				d[j]=1
	print(d)
fun()
