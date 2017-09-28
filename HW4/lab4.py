import re

fname= open("mbox-short.txt", "r")
flines= fname.readlines()
for line in flines:
	line= line.rstrip()
	if re.findall('From', line) :
		print (line)
		numbers= re.findall('[0-9]+', line) 
		print (numbers)
		name= re.findall('(\S*)@', line)
		print (name)


