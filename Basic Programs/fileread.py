filename=raw_input('enter file name')
fileid=open(filename)
c=fileid.read()
print c
print type(c)
