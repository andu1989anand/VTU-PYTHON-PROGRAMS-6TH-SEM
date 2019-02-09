fname=raw_input("enter a file name:")
fd=open(fname)
count=0
for line in fd:
    if line.startswith('From:'):
        line=line.split()
        print line[1]
        count+=1
print "number of lines starts with From: are=",count
   
