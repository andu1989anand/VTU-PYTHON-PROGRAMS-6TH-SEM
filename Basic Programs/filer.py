fname=raw_input("enter a file name:")
content=raw_input("enter a content to be written:")
fd=open(fname,'w')
fd.write(content)
fd=open(fname,'r')
rcontent=fd.read()
print rcontent
