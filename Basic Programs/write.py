filee=raw_input("enter a file name:")
content=raw_input("enter the content to be written:")
fd=open(filee,'w')
print fd
fd.write(content)
content=raw_input("enter the content to be written:")
fd.write(content)
fd.close
fd=open(filee)
c=fd.read()
print c
