class student:
	def __init__(self): # constructor..
		self.m=[]
		self.name=None
		self.age=None
		m=None
	def accept(self):
		self.name=input('name of student:')
		self.age=int(input('age of student:'))
		m1=int(input('marks in subject 1:'))
		m2=int(input('marks in subject 2:'))
		m3=int(input('marks in subject 3:'))
		self.m.append(m1)
		self.m.append(m2)
		self.m.append(m3)
		
	def display(self):
		print('name of student: '+self.name)
		print
		print('age of student: '+str(self.age))
		print('marks in 3 subjects:')
		for i in self.m:
			print(i)


if(__name__=='__main__'):
	s1=student()
	s1.accept()
	s1.display()
