def fun():
	d={'A':'apple','B':'ball','C':'cat','D':'dog',
	   'E':'elephant','F':'fish','G':'goat','H':'hen'}
	#key=input('enter your key: ')
	#value=input('enter your value: ')
	#d[key]=value
	#print(__name__)
	for i,j in d.items():
		print('key: ',i,' ','value: ',j)
	v=input('enter value to be searched in dictionary: ')
	if(v in d.values()):
		k=[k for k in d if(d[k]==v)] # using list comprehension.
		print(k,' ',v)
	else:
		print('not found.')
#fun()
#print(d.keys()) # dict_keys(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
#print(d.values()) # dict_values(['apple', 'ball', 'cat', 'dog', 'elephant', 'fish', 'goat', 'hen'])

#>>> d={'a':'abhi','m':'mandal'}
#>>> 'mandal' in d
#False
#>>> 'm' in d
#True
#>>> 'a' in d
#True
#>>> 'abhi' in d
#False
#>>> 
