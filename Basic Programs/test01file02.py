fd=open("b.txt")
line=fd.read()
print line
atpos=line.find('@')
spacepos=line.find(' ',atpos)
substring=line[atpos+1:spacepos]
print "substring is the file is:  ",substring
