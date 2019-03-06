from operator import itemgetter
class word:
	def __init__(self,sentence):
		self.sentence=sentence
	def reverse(self):
		s=""
		l=self.sentence.split()
		for i in range(len(l)-1,-1,-1):
			if(i!=0):
				s=s+l[i]+" "
			else:
				s=s+l[i]
		return s
	def count_vowel(self):
		count=0
		for i in self.sentence:
			if(i in ('a','e','i','o','u','A','E','I','O','U')):
				count+=1;
		return count

l=[]
s=word("i am here")
s1=s.reverse()
i=s.count_vowel()
l.append((s1,i))

p=word("hello world how are you")
p1=p.reverse()
j=p.count_vowel()
l.append((p1,j))

q=word("have a nice day")
q1=q.reverse() 
k=q.count_vowel()
l.append((q1,k))
l.sort(key=itemgetter(1),reverse=True)
#r=sorted(l,key=itemgetter(1),reverse=True)
#print(r)
for i in l:
	print(i[0]+'   vowel count: '+str(i[1]))			
	
# difference between sort and sorted.
#sorted() returns a new sorted list, leaving the original list unaffected.
#list.sort() sorts the list in-place, mutating the list indices, and returns None
#(like all in-place operations).
