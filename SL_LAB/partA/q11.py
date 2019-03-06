l=['0abhishek 00','1abhijeet 11','2sourav 22','3choudhary 33','4banerjee 44','5sunil 55','6danish 66','7shazib 77','8vivek 88','9adarsh 99','10ravi 1010',
   '11shivam 1111','12ajnay 1212','13shubhang 1313','14kaushik 1414','15vaibhav 1515','16harsh 1616','17vishrut 1717','18ankit 1818','19mohit 1919','20akshay 2020',
   '21akash 2121','22pandey 2222','23shubojit 2323','24vishwajit 2424','25kartik 2525','26yash 2626','27vallabh 2727','28aryaman 2828','29rohit 2929']

def extract(s):
	s1=""
	l=s.split()
	for i in l:
		if(not i.isalpha()):
			if(i.isdigit()):
				s1=s1+i+' '
			else:
				for j in i:
					if(j.isdigit()):
						s1=s1+j+' '
	return s1
	
for i in range (0,len(l)):
	s=l[i]
	print(s[::-1],end=' ')
	print('['+extract(s)+']',end=' ')
	if((i+1)%2==0 and (i+1)%3==0):
		print(l[i]+' '+l[i].upper())
		print('\n')
	elif((i+1)%2==0):
		print(l[i])
		print('\n')
	elif((i+1)%3==0):
		print(l[i].upper())
		print('\n')
	else:
		print('\n')
