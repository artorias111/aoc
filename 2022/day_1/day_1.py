#!/usr/bin/python3

f=open('in_file.txt','r')

s=[]
x=0 #temporary sum


for i in f:
	i=i.strip()
	if i=='':
		s.append(x)
		x=0
		continue
	x+=int(i)
s.append(x)

s.sort()
print(s)
print('***')
print(s[-1]+s[-2]+s[-3])
