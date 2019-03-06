'''
import operator
s=input("enter your text:")
l=s.split()
l.reverse()
ns=' '.join(l)
print(ns)

vowel=['a','A','e','E','i','I','o','O','u','U']
d={}
for i in l:
	count=0
	for letter in i:
		if(letter in vowel):
			count+=1
	d[i]=count
#print(d)
sorted_dict = sorted(d.items(),key=operator.itemgetter(1),reverse=True)

print(sorted_dict)

s=[]
for i in sorted_dict:
	s.append(i[0])

for a in range(0,len(s)):
	b=s[a]
	s[a]=b[::-1]

p=' '.join(s)
print(p)	
'''
import operator
vowel=['a','A','e','E','i','I','o','O','u','U']
class string:
	def __init__(self,sentence):
		self.sentence=sentence
	def count_vowel(self):
		count=0
		l=(self.sentence).split()
		for i in l:
			for letter in i:
				if(letter in vowel):
					count+=1
		return count
	
	def reverse(self):
		mylist=(self.sentence).split()
		list1=reversed(mylist)
		return list1

str1=string(input("first sentence"))
str2=string(input("second sentence"))
str3=string(input("third sentence"))

count1=str1.count_vowel()
count2=str2.count_vowel()
count3=str3.count_vowel()

ans1=str1.reverse()
s1=' '.join(ans1)
ans2=str2.reverse()
s2=' '.join(ans2)
ans3=str3.reverse()
s3=' '.join(ans3)
d={s1:count1, s2:count2, s3:count3}
sorted_dict = sorted(d.items(),key=operator.itemgetter(1),reverse=True)
print(sorted_dict)		
