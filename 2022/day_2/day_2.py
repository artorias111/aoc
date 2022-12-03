#!/usr/bin/python3

scores={'X':1,'Y':2,'Z':3}
f=open('in_file.txt','r')

win_dict={'A':'Y','B':'Z','C':'X'}
draw_dict={'A':'X','B':'Y','C':'Z'}
loss_dict={'A':'Z','B':'X','C':'Y'}

s=0

for i in f:
	i=i.strip()
	i=i.split()
	
	if i[1]=='X':
		s+=scores[loss_dict[i[0]]]
	if i[1]=='Y':
		s+=scores[draw_dict[i[0]]]
		s+=3
	if i[1]=='Z':
		s+=scores[win_dict[i[0]]]
		s+=6
		
print(s)
