from functools import reduce
l=[1,2,3,4,5,6]
m=[x*3 for x in l] #using list comprehension
print('list l: ',l)
print('list m: ',m)

#using reduce and lambda function
print('sum of list l: ',reduce(lambda a,b:a+b, l))
print('sum of list m: ',reduce(lambda a,b:a+b, m))

'''
A list comprehension generally consist of these parts :
   Output expression, 
   input sequence, 
   a variable representing member of input sequence and
   an optional predicate part. 

For example :

lst  =  [x ** 2  for x in range (1, 11)   if  x % 2 == 1] 

here, x ** 2 is output expression, 
      range (1, 11)  is input sequence, 
      x is variable and   
      if x % 2 == 1 is predicate part.
####################################################################

 A lambda function is a small anonymous function.

 A lambda function can take any number of arguments, but can only have one expression.
####Syntax#####
 lambda arguments : expression 

x = lambda a : a + 10  
print(x(5)) 

here x is a variable which is assigned a lambda function so now x is a function x(a) 
where a is the argument form the lambda function
'''
